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

        self.whitelistCookies = [
            '908b07ebedad40dd32e7828e481a40dd96ec4f8f3859fd80a0573dcb96202572', 
            '9e28c8ce837901ec3548dc667fb0b68c35e4d61904fe73c03eeb4578854b26e5', 
            '17fa43b574fa50a3e8eebfcbf971d08fb1c1cb72b34a15c61abefebd7c54e5ae']

    def setup(self):
        pass
        
    def playerJoinedServer(self):
        self.CURRENT_PLAYERS_AMOUNT += 1
    
    def playerLeftServer(self):
        self.CURRENT_PLAYERS_AMOUNT -= 1

    def checkHWID(self, cookie, hwid):
        pass

    def checkIP(self, cookie, ip):
        pass

    def checkMAC(self, cookie, mac):
        pass

    def checkPlayerLimit(self):
        if self.CURRENT_PLAYERS_AMOUNT >= self.CONCURRENT_PLAYERS_LIMIT:
            return False

        return True
    
    def checkPlayerLogin(self, cookie):
        ALLOW_ENTRY = self.checkPlayerLimit()

        #if cookie not in self.whitelistCookies:
        #    ALLOW_ENTRY = False

        if ALLOW_ENTRY:
            self.notify.info("Cookie '" + str(cookie) + "' has been allowed entry!")
        else:
            self.notify.warning("Cookie '" + str(cookie) + "' has been disallowed entry!")
        
        return ALLOW_ENTRY