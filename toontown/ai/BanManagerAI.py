from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class BanManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("BanManagerAI")

    def ban(self, acc, reason, time):
        pass
		
    def pban(self, acc, reason):
        pass
