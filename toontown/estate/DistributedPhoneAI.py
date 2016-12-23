from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedFurnitureItemAI import DistributedFurnitureItemAI
from toontown.toonbase import ToontownGlobals
from toontown.catalog import CatalogItem
from toontown.catalog.CatalogInvalidItem import CatalogInvalidItem
from toontown.catalog.CatalogItemList import CatalogItemList
from direct.distributed.ClockDelta import *
import time
from toontown.estate.PhoneGlobals import *

class DistributedPhoneAI(DistributedFurnitureItemAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPhoneAI")

    def __init__(self, air, furnitureMgr, item):
        DistributedFurnitureItemAI.__init__(self, air, furnitureMgr, item)
        self.avId = None
        self.inUse = False
        self.currAvId = 0

    def calcHouseItems(self, avatar):
        houseId = avatar.houseId
        
        if not houseId:
            self.notify.warning('Avatar %s has no houseId associated.' % avatar.doId)
            return 0
            
        house = simbase.air.doId2do.get(houseId)
        if not house:
            self.notify.warning('House %s (for avatar %s) not instantiated.' % (houseId, avatar.doId))
            return 0
            
        mgr = house.interior.furnitureManager
        attic = (mgr.atticItems, mgr.atticWallpaper, mgr.atticWindows)
        numHouseItems = len(CatalogItemList(house.getInteriorItems(), store=CatalogItem.Customization | CatalogItem.Location))
        numAtticItems = sum(len(x) for x in attic)
        
        return numHouseItems + numAtticItems

    def setInitialScale(self, sx, sy, sz):
        pass

    def getInitialScale(self):
        return (0.8, 0.8, 0.8)

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if self.inUse:
            self.ejectAvatar(avId)
            return
            
        av = self.air.doId2do.get(avId)
        if av:
            self.setInUse(avId)
            self.sendUpdateToAvatarId(avId, 'setLimits', [self.calcHouseItems(av)])
            self.d_setMovie(PHONE_MOVIE_PICKUP, avId)
            av.b_setCatalogNotify(0, av.mailboxNotify)
            
            self.air.questManager.toonCalledClarabelle(av)
            
    def avatarExit(self):
        if not self.inUse:
            self.notify.warning('Requested avatarExit but phone isn\'t in use!')
            return
        avId = self.air.getAvatarIdFromSender()
        if avId != self.currAvId:
            self.notify.warning('Requested avatarExit from unknown avatar %s' %avId)
            return
        self.d_setMovie(PHONE_MOVIE_HANGUP, avId)
        taskMgr.doMethodLater(1, self.resetMovie, self.taskName('resetMovie'))
        self.setFree()
        
    def setFree(self):
        self.inUse = False
        self.currAvId = 0
        
    def setInUse(self, avId):
        self.inUse = True
        self.currAvId = avId

    def d_setMovie(self, movie, avId):
        self.sendUpdate('setMovie', args=[movie, avId, globalClockDelta.getRealNetworkTime(bits=32)])

    def resetMovie(self, task):
        self.d_setMovie(PHONE_MOVIE_CLEAR, 0)
        return task.done

    def requestPurchaseMessage(self, context, item, optional):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.avId:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Tried to purchase while not using the phone!')
            return
        av = self.air.doId2do.get(avId)

        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, issue='Used phone from other shard!')
            return

        item = CatalogItem.getItem(item)
        if isinstance(item, CatalogInvalidItem): 
            self.air.writeServerEvent('suspicious', avId=avId, issue='Tried to purchase invalid catalog item.')
            return
        if item in av.backCatalog:
            price = item.getPrice(CatalogItem.CatalogTypeBackorder)
        elif item in av.weeklyCatalog or item in av.monthlyCatalog:
            price = item.getPrice(0)
        else:
            return

        if item.getDeliveryTime():
            if len(av.onOrder) > 3: #TODO correct number
                self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_OnOrderListFull])
                return
            if len(av.mailboxContents) + len(av.onOrder) >= ToontownGlobals.MaxMailboxContents:
                self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_MailboxFull])
            if not av.takeMoney(price):
                return
            item.deliveryDate = int(time.time()/60) + item.getDeliveryTime()
            av.onOrder.append(item)
            av.b_setDeliverySchedule(av.onOrder)
            self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_ItemOnOrder])
        else:
            if not av.takeMoney(price):
                #u wot m8
                return

            resp = item.recordPurchase(av, optional)
            if resp < 0: # refund if purchase unsuccessful
				av.addMoney(price)

            self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, resp])


    def requestPurchaseResponse(self, todo0, todo1):
        pass

    def requestGiftPurchaseMessage(self, todo0, todo1, todo2, todo3):
        pass

    def requestGiftPurchaseResponse(self, todo0, todo1):
        pass
