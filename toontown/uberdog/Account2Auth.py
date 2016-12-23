from SocketServer import TCPServer, BaseRequestHandler
from direct.directnotify.DirectNotifyGlobal import *
import threading, json
import pyotp

'''
Example Packet Structure:

  Request Login:
    {"type":"request-login", "username":"username"}

  Response Login:
    {"type":"response-login_resp", "result":"access-denied", "reason": "No accounts with that credentials were found in the database, perhapse you mispelled your username."}

'''

BUFFERSIZE = 1024
QUEUESIZE = 10000
ALLOWREUSE = True

requestTypes = [
    'request-login',
    'request-login_resp',
    'request-create',
    'request-invalid',
    'request-heartbeat'
]

class RequestHandler(BaseRequestHandler):
    notify = directNotify.newCategory("RequestHandler")
    notify.setInfo(True)
    notify.setWarning(True)

    def handle(self):
        data = str(self.request.recv(BUFFERSIZE))
        if len(data) == 0:
            return
        
        jdata = json.loads(data)

        try:
            requestType = jdata['type']
        except:
            self.notify.warning('Recieved an invalid requestType!')
            response = {
                "type":"response-invalid", "result":"invalid-request", "reason":"The request type provided was invalid, or your structure is invalid."
            }
            self.sendResponse(json.dumps(response))
            return

        if requestType == requestTypes[0]:
            self.requestLogin(jdata['username'])
        elif requestType == requestTypes[2]:
            # TODO: handle account creation...
            self.requestCreate()
        elif requestType == requestTypes[4]:
            response = {
                "type":"response-heartbeat", "result":"server-online", "reason":"Pong!"
            }
            self.sendResponse(json.dumps(response))
            return

    def requestLogin(self, username):
        with open('db-storage.json', 'rb') as storage:
            jdata = json.load(storage)
            accounts = jdata['Accounts']
            # We're done close the storage file.
            storage.close()

        if username in accounts:
            otpKey = pyotp.TOTP('%s%s' % (str(username).upper(), "2"))
            response = {
                "type":"response-login_resp", "result":"access-granted", "reason":str(username) + str(otpKey.now())
            }

            self.sendResponse(json.dumps(response))
            return

        response = {
            "type":"response-login_resp", "result":"access-denied", "reason": "No accounts with that credentials were found in the database, perhapse you mispelled your username."
        }

        self.sendResponse(json.dumps(response))
        return

    def requestCreate(self):
        return NotImplementedError
            
    def sendResponse(self, response):
        if len(response) == 0:
            return

        self.request.send(response)

class Account2Auth(TCPServer):
    TCPServer.request_queue_size = QUEUESIZE
    TCPServer.allow_reuse_address = ALLOWREUSE
    notify = directNotify.newCategory("Account2Auth")
    notify.setInfo(True)

    def __init__(self, host, port):
        TCPServer.__init__(self, (host, port), RequestHandler)
        self.hostDetails = [host, port]

    def startServer(self):
        self.process = threading.Thread(target=self.serve_forever)
        self.process.daemon = True
        self.process.start()
        self.notify.info('Authenication Service started on: %s:%d' % (self.hostDetails[0], self.hostDetails[1]))

    def stopServer(self):
        if self.process:
            self.process = None
            del self.process

        self.notify.info('Stopping Service, please wait...')
        self.shutdown()
        self.server_close()
