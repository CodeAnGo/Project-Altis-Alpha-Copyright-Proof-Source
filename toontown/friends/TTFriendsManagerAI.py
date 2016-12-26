from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify.DirectNotifyGlobal import directNotify

class TTFriendsManagerAI(DistributedObjectGlobalAI):
    notify = directNotify.newCategory('TTFriendsManagerUD')

    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)

    def requestToonStateUDtoAI(self, sender, avId):
        if avId not in self.air.doId2do.keys():
            # requested toon state for invalid doId!
            return

        # send back toon state to sender
        self.d_recieveToonState(sender, self.air.doId2do[avId].getAnimState())

    def d_recieveToonState(self, sender, state):
        self.sendUpdateToAvatarId(sender, 'recieveToonState', [
            state])