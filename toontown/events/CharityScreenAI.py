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
        threading.Thread(target=taskMgr.add, args=(self.getJson, 'jsonTask')).start()
        
    def getJson(self, task):
        information = httplib.HTTPConnection('www.projectaltis.com')
        information.request('GET', '/api/getcogs')
        info = json.loads(information.getresponse().read())
        self.count = info['counter']
        self.b_setCount(self.count)
        taskMgr.doMethodLater(10, self.getJson, 'jsonTask')
        
    def setCount(self, count):
        pass
        
    def b_setCount(self, count):
        self.d_setCount(count)
        self.setCount(count)
        
    def d_setCount(self, count):
        self.sendUpdate('setCount', [self.count])
        
    def unload(self):
        taskMgr.remove('jsonTask')
