'''
Created on Dec 30, 2016

@author: Drew
'''
from panda3d.core import Vec4
from direct.interval.IntervalGlobal import * 
from toontown.toon import Toon, ToonDNA
from direct.actor.Actor import Actor
from toontown.chat.ChatGlobals import *
from toontown.nametag.NametagGroup import *
from direct.gui.DirectGui import *

class CreditsScreen:
    '''
    The ending of the event, the all original credits sequence that no other server has ever put at the end of an event!
    '''


    def __init__(self):
        '''
        Setup the screen
        '''
        self.creditObjects = []


    def createCreditObject(self, imagepos = 'left', name = 'Toon', dna, pose = 'neutral'):
        '''
        Create a credit object using the specified image side, and toon data
        '''
        
        # After all this, we want to add the object to the list of objs
        self.creditObjects.append(obj)