from direct.distributed.DistributedObject import DistributedObject
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal

class BanManager(DistributedObject):
    neverDisable = 1
    notify = directNotify.newCategory('BanManager')
		
    def ban(self, todo1, todo2, todo3):
        pass
		
    def pban(self, acc, reason):
        pass
