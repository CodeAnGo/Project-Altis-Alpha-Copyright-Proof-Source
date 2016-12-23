from toontown.suit.DistributedSuitPlannerAI import DistributedSuitPlannerAI
from toontown.building.DistributedBuildingMgrAI import DistributedBuildingMgrAI
from toontown.environment import DistributedDayTimeManagerAI
from toontown.dna.DNAParser import DNAStorage, DNAGroup, DNAVisGroup
from toontown.environment import DistributedRainManagerAI

class StreetAI:
    """
    AI-side representation of everything in a single street.

    One subclass of this class exists for every neighborhood in the game.
    StreetAIs are responsible for spawning all SuitPlanners, ponds, and other
    street objects, etc.
    """
    
    def __init__(self, air, zoneId):
        self.air = air
        self.zoneId = zoneId
        
        # If it is a time where we want snow
        self.wantSnow = True
        
        dnaStore = DNAStorage()
        self.air.dnaStoreMap[self.zoneId] = dnaStore
        self.spawnObjects()
        self.createTime()
        self.createRain()

    def spawnObjects(self):
        filename = self.air.genDNAFileName(self.zoneId)
        self.air.dnaSpawner.spawnObjects(filename, self.zoneId)
        self.buildingMgr = DistributedBuildingMgrAI(self.air, self.zoneId, self.air.dnaStoreMap[self.zoneId], self.air.trophyMgr)
        self.sp = DistributedSuitPlannerAI(self.air, self.zoneId)
        self.sp.generateWithRequired(self.zoneId)
        self.sp.d_setZoneId(self.zoneId)
        self.sp.initTasks()
        
    def createTime(self):
        if self.zoneId not in [9100, 9200]:
            self.dayTimeMgr = DistributedDayTimeManagerAI.DistributedDayTimeManagerAI(self.air)
            self.dayTimeMgr.generateWithRequired(self.zoneId)  
            self.dayTimeMgr.start()

    def createRain(self):
        self.rainMgr = DistributedRainManagerAI.DistributedRainManagerAI(self.air)
        self.rainMgr.generateWithRequired(self.zoneId)  
        if self.zoneId in [1100, 1200, 1300] or self.wantSnow:
            self.rainMgr.start(True) # We want it to always rain in donalds dock
        else:
            self.rainMgr.start(False)
