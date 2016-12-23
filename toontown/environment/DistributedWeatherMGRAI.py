from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import globalClockDelta
from direct.fsm.FSM import FSM
from otp.ai.MagicWordGlobal import *
from direct.interval.IntervalGlobal import *

class DistributedWeatherMGRAI(DistributedObjectAI, FSM):
    notify = directNotify.newCategory('DistributedWeatherMGRAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, self.__class__.__name__)
        self.currSeq = None
        self.currTime = 0

        self.participants = []

    def start(self):
        self.sendUpdate('start', [])
   
    def setState(self, state):
        self.request(state)

    def d_setState(self, state):
        self.sendUpdate('setState', [state, globalClockDelta.getRealNetworkTime(bits=32)])
        if state is not 'Rain' or state is not 'Sunny':
            self.currTime = int(self.getCurrTime())
            # TODO: Send an update containing current time of the playing sequence
        
    def b_setState(self, state):
        self.setState(state)
        self.d_setState(state)
        
    def getState(self):
        return self.state

    def getCurrTime(self):
        if self.currSeq != None:
            return self.currSeq.getT()
        else:
            return 0
        
@magicWord(category=CATEGORY_SYSADMIN, types=[str])
def dayTime(state):
    invoker = spellbook.getInvoker()
    mangr = None
    for do in simbase.air.doId2do.values():
        if isinstance(do, DistributedWeatherMGRAI):
            mangr = do
            mangr.b_setState(state)
            break
   
            return 'time state set to %s.' % state
