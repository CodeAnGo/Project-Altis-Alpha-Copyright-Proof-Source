from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toonbase import ToontownGlobals

# Import the Catalog
from toontown.catalog import CatalogItem
from toontown.catalog.CatalogItemList import CatalogItemList
from toontown.catalog.CatalogPoleItem import CatalogPoleItem
from toontown.catalog.CatalogBeanItem import CatalogBeanItem
from toontown.catalog.CatalogChatItem import CatalogChatItem
from toontown.catalog.CatalogClothingItem import CatalogClothingItem, getAllClothes
from toontown.catalog.CatalogAccessoryItem import CatalogAccessoryItem
from toontown.catalog.CatalogRentalItem import CatalogRentalItem
from toontown.catalog.CatalogInvalidItem import CatalogInvalidItem

import time

class TTCodeRedemptionMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("TTCodeRedemptionMgrAI")

    # Contexts
    Success = 0
    InvalidCode = 1
    ExpiredCode = 2
    Ineligible = 3
    AwardError = 4
    TooManyFails = 5
    ServiceUnavailable = 6

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def delete(self):
        DistributedObjectAI.delete(self)

    def giveAwardToToonResult(self, todo0, todo1):
        pass

    def redeemCode(self, context, code):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Tried to redeem a code from an invalid avId')
            return

        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Invalid avatar tried to redeem a code')
            return

        # Some constants
        valid = True
        eligible = True
        expired = False
        delivered = False

        # Get our redeemed codes
        codes = av.getRedeemedCodes()
        print codes
        if not codes:
            codes = [code]
            av.setRedeemedCodes(codes)
        else:
            if not code in codes:
                codes.append(code)
                av.setRedeemedCodes(codes)
                valid = True
            else:
                valid = False

        # Is the code valid?
        if not valid:
            self.air.writeServerEvent('code-redeemed', avId=avId, issue='Invalid code: %s' % code)
            self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, self.InvalidCode, 0])
            return

        # Did our code expire?
        if expired:
            self.air.writeServerEvent('code-redeemed', avId=avId, issue='Expired code: %s' % code)
            self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, self.ExpiredCode, 0])
            return

        # Are we able to redeem this code?
        if not eligible:
            self.air.writeServerEvent('code-redeemed', avId=avId, issue='Ineligible for code: %s' % code)
            self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, self.Ineligible, 0])
            return

        # Iterate over these items and deliver item to player
        items = self.getItemsForCode(code)
        for item in items:
            if isinstance(item, CatalogInvalidItem): # Umm, u wot m8?
                self.air.writeServerEvent('suspicious', avId=avId, issue='Invalid CatalogItem\'s for code: %s' % code)
                self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, self.InvalidCode, 0])
                break

            if len(av.mailboxContents) + len(av.onGiftOrder) >= ToontownGlobals.MaxMailboxContents:
                # Mailbox is full
                delivered = False
                break

            item.deliveryDate = int(time.time() / 60) + 1 # Let's just deliver the item right away.
            av.onOrder.append(item)
            av.b_setDeliverySchedule(av.onOrder)
            delivered = True

        if not delivered:
            # 0 is Success
            # 1, 2, 15, & 16 is an UnknownError
            # 3 & 4 is MailboxFull
            # 5 & 10 is AlreadyInMailbox
            # 6, 7, & 11 is AlreadyInQueue
            # 8 is AlreadyInCloset
            # 9 is AlreadyBeingWorn
            # 12, 13, & 14 is AlreadyReceived
            self.air.writeServerEvent('code-redeemed', avId=avId, issue='Could not deliver items for code: %s' % code)
            self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, self.InvalidCode, 0])
            return

        # Send the item and tell the user its A-Okay
        self.air.writeServerEvent('code-redeemed', avId=avId, issue='Successfuly redeemed code: %s' % code)
        self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, self.Success, 0])

    def getItemsForCode(self, code):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Could not parse the gender of an invalid avId')
            return

        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Could not parse the gender of an invalid avatar')
            return

        '''
        # Here is an example of giving clothing to specific genders.
        if code == "GenderExample":
            # The following code will check to see if the gender is a male.
            # If it is, then they will be given shirt 2002.
            if av.getStyle().getGender() == 'm':
                shirt = CatalogClothingItem(2002, 0)
            # If it sees the gender isn't male, it will give shirt 2003.
            else:
                shirt = CatalogClothingItem(2003, 0)
            return [shirt]
        '''

        code = code.lower() 

        if code == "cannons":
            rent = CatalogRentalItem(ToontownGlobals.RentalCannon, 48*60, 0)
            return [rent]

        return []

    def requestCodeRedeem(self, todo0, todo1):
        pass

    def redeemCodeResult(self, todo0, todo1, todo2):
        pass
