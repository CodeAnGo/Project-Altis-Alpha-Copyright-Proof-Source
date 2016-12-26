from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify.DirectNotifyGlobal import directNotify

class ClientServicesManagerAI(DistributedObjectGlobalAI):

    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)

    def requestBanPlayer(self, avId, reason):
        self.sendUpdate('requestBanPlayer', [avId, reason])