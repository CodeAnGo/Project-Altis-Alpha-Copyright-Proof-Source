from panda3d.core import *
from panda3d.direct import *
from direct.directnotify import DirectNotifyGlobal
from otp.launcher.LauncherBase import LauncherBase
import os
import sys
import time
import json

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)
        
class LogAndOutput:
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()

    def flush(self):
        self.log.flush()
        self.orig.flush()

class TTLauncher(LauncherBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownDummyLauncher')

    def __init__(self):
        self.http = HTTPClient()

        self.logPrefix = 'altis-'

        ltime = 1 and time.localtime()
        logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2],
                                                   ltime[3], ltime[4], ltime[5])

        
        if not os.path.exists('logs/'):
            os.mkdir('logs/')
            self.notify.info('Made new directory to save logs.')
        
        logfile = os.path.join('logs', self.logPrefix + logSuffix + '.log')

        log = open(logfile, 'a')
        logOut = LogAndOutput(sys.stdout, log)
        logErr = LogAndOutput(sys.stderr, log)
        sys.stdout = logOut
        sys.stderr = logErr

    def getPlayToken(self):
        username = self.getValue('TT_USERNAME')
        password = self.getValue('TT_PASSWORD')
        import urllib2
        url = "http://projectaltis.com/api/?u="+str(username)+"&p="+str(password) # As account is already in DBM, we need to CHECK it's level
        output = urllib2.urlopen(url).read()
        jsonDeserialed = Payload(output)
        if jsonDeserialed.status == "critical":
            print(jsonDeserialed.reason)
            print(jsonDeserialed.additional)
            raise SystemExit
        if jsonDeserialed.status == "false":
            print(jsonDeserialed.reason)
            print(jsonDeserialed.additional)
            raise SystemExit
        if jsonDeserialed.status == "true":
            return jsonDeserialed.additional
        else:
            raise SystemExit
        
    def getGameServer(self):
        return self.getValue('TT_GAMESERVER')

    def setPandaErrorCode(self, code):
        pass

    def getGame2Done(self):
        return True

    def getLogFileName(self):
        return 'toontown'

    def getValue(self, key, default = None):
        return os.environ.get(key, default)

    def setValue(self, key, value):
        os.environ[key] = str(value)

    def getVerifyFiles(self):
        return config.GetInt('launcher-verify', 0)

    def getTestServerFlag(self):
        return self.getValue('IS_TEST_SERVER', 0)

    def isDownloadComplete(self):
        return 1

    def isTestServer(self):
        return 0

    def getPhaseComplete(self, phase):
        return 1

    def startGame(self):
        self.newTaskManager()
        eventMgr.restart()
        from toontown.toonbase import ToontownStart
