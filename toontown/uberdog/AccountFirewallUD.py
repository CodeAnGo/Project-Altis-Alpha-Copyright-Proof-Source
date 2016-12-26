from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify
import os
import json
#info, debug, warning, error

class AccountFirewallUD:
    notify = directNotify.newCategory('AccountFirewall')
    CONCURRENT_PLAYERS_LIMIT = 500
    CURRENT_PLAYERS_AMOUNT = 0

    def __init__(self, air):
        self.notify.info("Successfully started!")
        self.air = air

    def setup(self):
        pass
        
    def playerJoinedServer(self):
        self.CURRENT_PLAYERS_AMOUNT += 1
        return
    
    def playerLeftServer(self):
        self.CURRENT_PLAYERS_AMOUNT -= 1
        return

    def checkHWID(self, cookie, hwid):
        pass

    def checkIP(self, cookie, ip):
        pass

    def checkMAC(self, cookie, mac):
        pass

    def checkPlayerLimit(self):
        if self.CURRENT_PLAYERS_AMOUNT < self.CONCURRENT_PLAYERS_LIMIT:
            return True
        elif self.  CURRENT_PLAYERS_AMOUNT >= self.CONCURRENT_PLAYERS_LIMIT:
            return False
    
    def checkPlayerLogin(self, cookie):
        ALLOW_ENTRY = False
        ALLOW_ENTRY = self.checkPlayerLimit()

        if ALLOW_ENTRY:
            self.notify.info("Cookie '" + str(cookie) + "' has been allowed entry!")
        else:
            self.notify.warning("Cookie '" + str(cookie) + "' has been disallowed entry!")
        return ALLOW_ENTRY
    
