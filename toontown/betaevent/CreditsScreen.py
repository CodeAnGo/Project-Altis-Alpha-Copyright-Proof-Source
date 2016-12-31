'''
Created on Dec 30, 2016

@author: Drew
'''
from panda3d.core import Vec4, TransparencyAttrib, Point3, VBase3
from direct.interval.IntervalGlobal import * 
from toontown.toon import Toon, ToonDNA
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from CreditsLines import *

class CreditsScreen:
    '''
    The ending of the event, the all original credits sequence that no other server has ever put at the end of an event!
    '''


    def __init__(self):
        '''
        Setup the screen
        '''
        self.creditsSequence = None
        self.logo = OnscreenImage(image='phase_3/maps/toontown-logo.png',
                                  scale=(1.0 * (4.0/3.0), 1, 1.0 / (4.0/3.0)),
                                  pos=(0, 0, 0))
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        self.logo.reparentTo(aspect2d)
        self.logo.hide()
        self.logo.setColorScale(1, 1, 1, 0)

    def startCredits(self):
        base.musicManager.stopAllSounds()
        self.music = loader.loadMusic('phase_3/audio/bgm/downloader.ogg')
        base.playMusic(self.music, looping = 1)

        self.creditsSequence = Sequence(
            Wait(2),
            Func(base.localAvatar.stopUpdateSmartCamera),
            Func(base.camera.wrtReparentTo, render),
            Func(base.transitions.letterboxOn, 1),
            base.camera.posHprInterval(3, Point3(0, 0, 10), VBase3(0, 90, 0)),
            Func(self.logo.show),
            LerpColorScaleInterval(self.logo, 2, Vec4(1, 1, 1, 1)),
            Wait(2),
            LerpColorScaleInterval(self.logo, 2, Vec4(1, 1, 1, 0)),
            Func(self.logo.hide)).start()
            
    def displayText(self, person):
        # Person is imported from CreditLines, which has a dict
        # Each DICT has the name, and the position
        
        # Open and split it out for use
        name, position = person