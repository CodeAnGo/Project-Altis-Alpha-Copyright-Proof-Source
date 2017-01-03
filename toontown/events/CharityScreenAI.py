from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from direct.task import Task
import json, httplib
from toontown.pgui.DirectGui import DirectLabel
from panda3d.core import *
from direct.interval.IntervalGlobal import * 
import threading

class CharityScreenAI(DistributedObjectAI):
    notify = directNotify.newCategory('CharityScreenAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        
    def start(self):
        taskMgr.add(self.updateJsonTask, 'jsonTask')
         
    def updateJsonTask(self, task):
        threading.Thread(target=self.getJson).start()
        taskMgr.doMethodLater(10, self.updateJsonTask, 'jsonTask')
        
    def getJson(self):
        information = httplib.HTTPConnection('www.projectaltis.com')
        information.request('GET', '/api/getcogs')
        info = json.loads(information.getresponse().read())
        self.count = info['counter']
        self.sendUpdate('setCount', [self.count])
        
    def setCount(self):
        pass
        
    def b_setCount(self):
        pass
        
    def d_setCount(self):
        pass
        
    def unload(self):
        taskMgr.remove('jsonTask')
