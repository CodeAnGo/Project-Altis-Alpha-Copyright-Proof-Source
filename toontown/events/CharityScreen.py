from direct.distributed.DistributedObject import DistributedObject
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from direct.task import Task
import json, httplib
from toontown.pgui.DirectGui import DirectLabel
from panda3d.core import *
from direct.interval.IntervalGlobal import * 
import threading

class CharityScreen(DistributedObject):
    notify = directNotify.newCategory('CharityScreen')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.zone2pos = {
            ToontownGlobals.ToontownCentral : (40, 0, 25),
            ToontownGlobals.DonaldsDock : (-25, 17, 25),
            ToontownGlobals.DaisyGardens : (5, 137, 25),
            ToontownGlobals.MinniesMelodyland : (0, 0, 8),
            ToontownGlobals.TheBrrrgh : (-111, -44, 25),
            ToontownGlobals.DonaldsDreamland : (0, 0, 6)}
        self.bob = None
        self.screenObject = None
        self.counter = None

    def announceGenerate(self):
        self.cr.chairityEvent = self

    def start(self, zoneId):
        def startScreen(*args):
            self.screenObject = args[0]
            self.screenObject.reparentTo(render)
            if ZoneUtil.getHoodId(zoneId) == ToontownGlobals.MinniesMelodyland:
                self.screenObject.reparentTo(self.cr.playGame.getPlace().loader.geom.find('**/center_icon'))
            self.screenObject.setPos(self.zone2pos.get(ZoneUtil.getHoodId(zoneId), (0, 0, 6)))
            self.screenObject.setHpr(-90, 0, 0)
            self.counter = DirectLabel(parent = render, pos = (0, 0, 0), relief = None, text = '10 cogs destroyed = $0.01\nto Child\'s Play Charity\n(Max $15,000)\nCheck website for more details!', text_scale = 1, text_fg = (1, 1, 1, 1) , text_align = TextNode.ACenter, text_font = ToontownGlobals.getMinnieFont())
            self.counter.reparentTo(self.screenObject)
            self.counter.setPos(self.screenObject.find("**/front_screen").getPos() + Point3(0.0, -1.5, 0.3)) 
            
            self.counterback = DirectLabel(parent = render, pos = (0, 0, 0), relief = None, text = '10 cogs destroyed = $0.01\nto Child\'s Play Charity\n(Max $15,000)\nCheck website for more details!', text_scale = 1, text_fg = (1, 1, 1, 1) , text_align = TextNode.ACenter, text_font = ToontownGlobals.getMinnieFont())
            self.counterback.reparentTo(self.screenObject)
            self.counterback.setPos(self.screenObject.find("**/back_screen").getPos() + Point3(0.0, 1.5, 0.3))
            self.counterback.setHpr(180, 0, 0)
            
        asyncloader.loadModel("phase_3.5/models/events/charity/flying_screen.bam", callback = startScreen)
        
    def setCount(self, count):
        self.count = count
        if self.counter and self.counterback:
            self.counter['text'] = (str(self.count) + "\nCogs Destroyed")
            self.counterback['text'] = (str(self.count) + "\nCogs Destroyed")
            
    def unload(self):
        print("unload")
        self.ignoreAll()
        if self.screenObject:
            self.screenObject.removeNode()
            self.screenObject = None       
    def delete(self):
        self.cr.chairityEvent = None
        print("delete")
        if self.screenObject:
            self.screenObject.removeNode()
            self.screenObject = None