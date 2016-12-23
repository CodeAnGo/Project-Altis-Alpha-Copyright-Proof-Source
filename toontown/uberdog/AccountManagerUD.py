from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from direct.fsm.FSM import *
from time import gmtime, strftime
import base64, os, json

class Operation(FSM):
    def __init__(self, accMgr, conn, token):
        FSM.__init__(self, self.__class__.__name__)
        self.accMgr = accMgr
        self.air = self.accMgr.air
        self.connectionId = conn
        self.token = token
        
    def killConnection(self, reason):
        self.accMgr.killConnection(self.connectionId, reason)
        self.demand("Off")
        
    def enterOff(self):
        del self.accMgr.connection2operation[self.connectionId]

class AccountOperation(Operation):
    def enterStart(self):
        (ret, data) = self.accMgr.checkIfStored(self.token)
        if ret == 'failure':
            self.demand("Create")
            return
            # In production, we'd have to drop the connection, but since we are
            # under dev stage, let anyone connect with any account.
            self.killConnection("Your cookie was rejected.")
            return
        if not data:
            self.demand("Create")
        else:
            self.accountId = data
            self.demand("QueryAccount")
            
    def enterQueryAccount(self):
        self.air.dbInterface.queryObject(self.accMgr.dbId, self.accountId, self.__handleRetrieve)
        
    def __handleRetrieve(self, dclass, fields):
        if dclass != self.air.dclassesByName['AccountManagerUD']:
            self.killConnection('Account object not found in the database.')
            return
        self.account = fields
        self.avList = self.account["ACCOUNT_AVATARS"]
        self.demand("QueryToons")
        
    def enterCreate(self):
        self.account = {
            'ACCOUNT_AVATARS': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'ACCOUNT_USERNAME': self.token,
            'ACCOUNT_TIME_CREATED': strftime("%Y-%m-%d %H:%M:%S", gmtime()),
            'ACCOUNT_LAST_LOGIN': strftime("%Y-%m-%d %H:%M:%S", gmtime())
        }

        self.accMgr.air.dbInterface.createObject(self.accMgr.dbId, 
                                    dclass=self.air.dclassesByName['AccountManagerUD'], 
                                    fields=self.account, 
                                    callback=self._createdAccount)

    def _createdAccount(self, accId):
        self.accountId = accId
        self.avList = self.account["ACCOUNT_AVATARS"]
        self.demand("UpdateAccount")

    def enterUpdateAccount(self):
        self.accMgr._updateAccountOnCreation(self.token, self.accountId)
        self.demand("QueryToons")
        
    def enterQueryToons(self):
        self.toonsQueue = set()
        self.toonFields = {}
        for avId in self.avList:
            if avId:
                self.toonsQueue.add(avId)
                def handleResp(dclass, fields, avId=avId):
                    if self.state != 'QueryToons': 
                        return
                    if dclass != self.air.dclassesByName['DistributedToonUD']:
                        self.killConnection('Avatar is invalid!')
                        return
                    self.toonFields[avId] = fields
                    self.toonsQueue.remove(avId)
                    if not self.toonsQueue:
                        self.demand("SendToons")
                        
                self.air.dbInterface.queryObject(self.accMgr.dbId, avId,
                                                     handleResp)
        if not self.toonsQueue:
            self.demand('SendToons')
            
    def enterSendToons(self):
        avatars = []
        for avId, fields in self.toonFields.items():
            dna = fields["setDNAString"][0] #TODO: parse DNA and check if it's allowed
            name = fields["setName"][0] #TODO: name states
            avatars.append([avId, dna, name])
        self.potAvList = avatars
        self.demand("SetAccount")

    def enterSetAccount(self):
        datagram = PyDatagram()
        datagram.addServerHeader(self.connectionId, self.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
        datagram.addUint64(self.accMgr.GetAccountConnectionChannel(self.accountId)) # TODO!
        self.air.send(datagram)
        datagram.clear() # Cleanse data

        datagram = PyDatagram()
        datagram.addServerHeader(self.connectionId, self.air.ourChannel, CLIENTAGENT_SET_CLIENT_ID)
        datagram.addUint64(self.accountId << 32)
        self.air.send(datagram)
        datagram.clear() # Cleanse data

        datagram = PyDatagram()
        datagram.addServerHeader(self.connectionId, self.air.ourChannel, CLIENTAGENT_SET_STATE)
        datagram.addUint16(2) # ESTABLISHED
        self.air.send(datagram)
        datagram.clear() # Cleanse data
        
        fields = {
            'ACCOUNT_LAST_LOGIN': strftime("%Y-%m-%d %H:%M:%S", gmtime())
        }

        self.air.dbInterface.updateObject(databaseId=self.accMgr.dbId,
                                        doId=self.accountId,
                                        dclass=self.air.dclassesByName['AccountManagerUD'],
                                        newFields=fields)

        # We're done here send a response.
        self.accMgr.sendUpdateToChannel(self.connectionId, 'recieveAvatar', [self.potAvList])
        self.demand("Off")


class AccountManagerUD(DistributedObjectGlobalUD):
    dbStorageFilename = 'db-storage.json'
    dbStoreStucture = {
        'Accounts': {
        }
    }

    dbId = 4003 # look to the astron config.

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)
        self.playToken2connection = { }
        self.accountId2connection = { }
        self.connection2operation = {}
        self.createStore()

    def createStore(self):
        if not os.path.exists(self.dbStorageFilename):
            with open(self.dbStorageFilename, 'w+') as store:
                json.dump(self.dbStoreStucture, store)
                store.close()

    def generateSeason(self):
        pass
        
    def killConnection(self, connectionId, reason):
        dg = PyDatagram()
        dg.addServerHeader(connectionId, self.air.ourChannel, CLIENTAGENT_EJECT)
        dg.addUint16(122)
        dg.addString(reason)
        self.air.send(dg)

    def requestLogin(self, token, password, key):
        sender = self.air.getMsgSender()
        if sender >> 32: # If already logged in
            self.killConnection(sender, "The current account is already logged in.")
            return
        if len(token) == 0:
            self.killConnection(sender, "Invalid token!")
            return
        
        if self.air.securityKeyEnabled:
            keyMatch = self.air.securityKey.match(key)
            if not keyMatch:
                self.killConnection(sender, "Invalid authentication key!")
                return

        if self.air.adminServiceEnabled:
            allowed = self.air.adminServiceUD.canLogin()
            if not allowed:
                self.killConnection(sender, "Server is currently down for mainternance!")
                return
            
        self.connection2operation[sender] = AccountOperation(self, sender, token)
        self.connection2operation[sender].request("Start")

    def checkIfStored(self, token):
        with open(self.dbStorageFilename, 'rb') as store:
            jdata = json.load(store)
            store.close()
        
        accounts = jdata['Accounts']
        if token in accounts:
            return ('success', accounts[token])

        return ('failure', None)

    def _updateAccountOnCreation(self, token, doId):
        with open(self.dbStorageFilename, 'r') as store:
            jdata = json.load(store)
            store.close()
        
        newData = jdata
        newData['Accounts'][token] = doId

        with open(self.dbStorageFilename, 'r+') as store:
            store.write(json.dumps(newData))
        
        