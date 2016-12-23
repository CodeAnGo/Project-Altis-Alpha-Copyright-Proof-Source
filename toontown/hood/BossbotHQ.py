from panda3d.core import Fog
import CogHood
from toontown.toonbase import ToontownGlobals
from toontown.coghq import BossbotCogHQLoader
from toontown.hood import ZoneUtil

class BossbotHQ(CogHood.CogHood):

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        CogHood.CogHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownGlobals.BossbotHQ
        self.cogHQLoaderClass = BossbotCogHQLoader.BossbotCogHQLoader
        self.storageDNAFile = None
        self.skyFile = 'phase_9/models/cogHQ/cog_sky'
        self.titleColor = (0.5, 0.5, 0.5, 1.0)
        return

    def load(self):
        CogHood.CogHood.load(self)
        self.sky.hide()
        self.fog = Fog('BossbotHQFog')
        self.sky.hide()
        self.parentFSM.getStateNamed('BossbotHQ').addChild(self.fsm)

    def unload(self):
        self.parentFSM.getStateNamed('BossbotHQ').removeChild(self.fsm)
        del self.cogHQLoaderClass
        CogHood.CogHood.unload(self)
        self.fog = None

    def enter(self, *args):
        CogHood.CogHood.enter(self, *args)
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.BossbotHQCameraNear, ToontownGlobals.BossbotHQCameraFar)
        self.setFog()

    def exit(self):
        localAvatar.setCameraFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        CogHood.CogHood.exit(self)

    def spawnTitleText(self, zoneId, floorNum = None):
        if ZoneUtil.isMintInteriorZone(zoneId):
            text = '%s\n%s' % (ToontownGlobals.StreetNames[zoneId][-1], TTLocalizer.MintFloorTitle % (floorNum + 1))
            self.doSpawnTitleText(text)
        else:
            CogHood.CogHood.spawnTitleText(self, zoneId)

    def setFog(self):
        if base.wantFog:
            self.fog.setColor(0.1, 0.1, 0.1)
            self.fog.setExpDensity(0.004)
            render.clearFog()
            render.setFog(self.fog)
            self.sky.clearFog()
            self.sky.setFog(self.fog)
