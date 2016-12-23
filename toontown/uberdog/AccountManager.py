from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from toontown.distributed.PotentialToon import  *
import pyotp, string, random

class AccountManager(DistributedObjectGlobal):

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)
        self.__totp = pyotp.TOTP("DEMOSECRET")
    
    def __generateSecurityKey(self):
        return self.__totp.now()
    
    def requestLogin(self, token, password):
        __key = self.__generateSecurityKey()
        self.sendUpdate('requestLogin', [token, password, int(__key)])

    def recieveAvatar(self, avList):
        avList = list(avList)
        newAvList = []
        for av in avList:
            pot = PotentialToon(avId=av[0], dna=av[1], name=av[2])
            newAvList.append(pot)
            
        messenger.send('loginDone', [newAvList])