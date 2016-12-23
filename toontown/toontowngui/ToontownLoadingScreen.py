from panda3d.core import *
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.hood import ZoneUtil
import random

class ToontownLoadingScreen:
    logoScale = (0.5, 1.0, 0.25)  # Scale for our logo.

    def __init__(self):
        self.__expectedCount = 0
        self.__count = 0
        self.loadingGui = None
        self.range = None
        self.loadingText = None
        self.background = None
        self.logo = None
        base.graphicsEngine.renderFrame()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + '\n' + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def begin(self, range, label, gui, tipCategory, zoneId):
        self.loadingGui = aspect2d.attachNewNode('loadingUI')
        self.loadingGui.reparentTo(aspect2d, 6000)
        self.logo = OnscreenImage(
            image='phase_3/maps/toontown-logo.png',
            scale=self.logoScale)
       
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        self.logo.setPos(0, 0, 0.65)
        self.loadingObj = OnscreenText(text='', align=TextNode.ACenter, scale=0.04, style = 3, fg = (1, 1, 1, 1))
        self.loadingObj.setPos(0, -.8)
        self.loadingText = OnscreenText(text='Initializing Load...', align=TextNode.ACenter, scale=0.1, pos=(0, 0, 0))
        self.loadingText.reparentTo(aspect2d)
        self.loadingText['text'] = label
        base.graphicsEngine.renderFrame()
        self.background = OnscreenImage(image = 'phase_3.5/maps/loading/toon.jpg', parent = aspect2d)
        self.background.setScale(2, 1, 1)
        self.background.show()
        self.background.wrtReparentTo(self.loadingGui)
        self.loadingText.wrtReparentTo(self.loadingGui)
        self.logo.wrtReparentTo(self.loadingGui)
        base.graphicsEngine.renderFrame()

    def destroy(self):
        pass
        
    def end(self):
        if self.loadingGui:
            self.loadingGui.removeNode()
            self.loadingGui = None
            
        if self.loadingText:
            self.loadingText.destroy()
            self.loadingText = None
            
        if self.background:
            self.background.destroy()
            self.background = None
            
        if self.logo:
            self.logo.destroy()
            self.logo = None
            
        return (self.__expectedCount, self.__count)

    def abort(self):
        self.loadingGui.reparentTo(hidden)
        self.loadingObj = None
        
    def tick(self):
        self.__count = self.__count + 1
        base.graphicsEngine.renderFrame()
