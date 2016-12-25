from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.distributed.PotentialAvatar import PotentialAvatar
from otp.otpbase import OTPLocalizer, OTPGlobals
from otp.margins.WhisperPopup import *
from panda3d.core import *
from panda3d.direct import *
import json
import requests

class ClientServicesManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('ClientServicesManager')

    systemMessageSfx = None
    avIdsReportedThisSession = []
    sessionKey = '1Cgb/DcqxgqXO5b62nHw+RQFVdOwl+i20AK1z5oTv8Z='

    # --- LOGIN LOGIC ---
    def performLogin(self, doneEvent):
        self.doneEvent = doneEvent

        urlResponse = requests.get('http://www.projectaltis.com/api/?u=%s&p=%s' % (base.launcher.getUsername(), 
            base.launcher.getPassword()))

        try:
            response = json.loads(urlResponse.text)
        except:
            self.notify.error('Failed to decode json login API response!')
            return

        # TODO: FIX ME - The JSON data is decoded as unicode so boolean types aren't redefined correctly
        if response['status'] != 'true':
            # couldn't find the details in the database!
            return
        else:
            # the request was successful, set the login cookie and login.
            cookie = response['additional']

        self.sendUpdate('login', [cookie, self.sessionKey])

    def acceptLogin(self):
        messenger.send(self.doneEvent, [{'mode': 'success'}])

    # --- AVATARS LIST ---
    def requestAvatars(self):
        self.sendUpdate('requestAvatars')

    def setAvatars(self, avatars):
        avList = []
        for avNum, avName, avDNA, avPosition, nameState, hp, maxHp, lastHood in avatars:
            nameOpen = int(nameState == 1)
            names = [avName, '', '', '']
            if nameState == 2: # PENDING
                names[1] = avName
            elif nameState == 3: # APPROVED
                names[2] = avName
            elif nameState == 4: # REJECTED
                names[3] = avName
            av = PotentialAvatar(avNum, names, avDNA, avPosition, nameOpen)
            av.hp = maxHp
            av.maxHp = maxHp
            av.lastHood = lastHood
            avList.append(av)
        self.cr.handleAvatarsList(avList)

    # --- AVATAR CREATION/DELETION ---
    def sendCreateAvatar(self, avDNA, _, index, uber):
        self.sendUpdate('createAvatar', [avDNA.makeNetString(), index, uber])

    def createAvatarResp(self, avId):
        messenger.send('nameShopCreateAvatarDone', [avId])

    def sendDeleteAvatar(self, avId):
        self.sendUpdate('deleteAvatar', [avId])

    # No deleteAvatarResp; it just sends a setAvatars when the deed is done.

    # --- AVATAR NAMING ---
    def sendSetNameTyped(self, avId, name, callback):
        self._callback = callback
        self.sendUpdate('setNameTyped', [avId, name])

    def setNameTypedResp(self, avId, status):
        self._callback(avId, status)

    def sendSetNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4, callback):
        self._callback = callback
        self.sendUpdate('setNamePattern', [avId, p1, f1, p2, f2, p3, f3, p4, f4])

    def setNamePatternResp(self, avId, status):
        self._callback(avId, status)

    def sendAcknowledgeAvatarName(self, avId, callback):
        self._callback = callback
        self.sendUpdate('acknowledgeAvatarName', [avId])

    def acknowledgeAvatarNameResp(self):
        self._callback()

    # --- AVATAR CHOICE ---
    def sendChooseAvatar(self, avId):
        self.sendUpdate('chooseAvatar', [avId])

    # No response: instead, an OwnerView is sent or deleted.

    def systemMessage(self, code, params):
        # First, format message:
        msg = OTPLocalizer.CRSystemMessages.get(code)
        if not msg:
            self.notify.warning('Got invalid system-message code: %d' % code)
            return

        try:
            message = msg % tuple(params)
        except TypeError:
            self.notify.warning(
                'Got invalid parameters for system-message %d: %r' % (code, params))
            return

        whisper = WhisperPopup(message, OTPGlobals.getInterfaceFont(), WhisperPopup.WTSystem)
        whisper.manage(base.marginManager)
        if not self.systemMessageSfx:
            self.systemMessageSfx = base.loadSfx('phase_4/audio/sfx/clock03.ogg')
        if self.systemMessageSfx:
            base.playSfx(self.systemMessageSfx)

    def hasReportedPlayer(self, avId):
        return avId in self.avIdsReportedThisSession

    def d_reportPlayer(self, avId, category):
        # Drop-in replacement for Disney's "CentralLogger" reporting object.
        if self.hasReportedPlayer(avId):
            # We've already reported this avId.
            return
        self.avIdsReportedThisSession.append(avId)
        self.sendUpdate('reportPlayer', [avId, category])
