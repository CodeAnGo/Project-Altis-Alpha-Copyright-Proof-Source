from direct.showbase.ShowBase import ShowBase
from panda3d.core import PandaNode, LightNode, TextNode
from panda3d.core import Filename, NodePath
from panda3d.core import PointLight, AmbientLight
from panda3d.core import LightRampAttrib, AuxBitplaneAttrib
from panda3d.core import CardMaker
from panda3d.core import Shader, Texture, TexturePool
from direct.task.Task import Task
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.showbase.BufferViewer import BufferViewer
from direct.filter.CommonFilters import CommonFilters
import sys
import os


# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1),
                        parent=base.a2dTopLeft, align=TextNode.ALeft,
                        pos=(0.08, -pos - 0.04), scale=.05)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, pos=(-0.1, 0.09), scale=.08,
                        parent=base.a2dBottomRight, align=TextNode.ARight,
                        fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1))


class TexturePView(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        print(str(sys.argv))
        self.model = loader.loadModel(str(sys.argv[1]))
        self.model.reparentTo(render)
        self.inst1 = addInstructions(0.06, "ESC: Quit")
        self.inst2 = addInstructions(0.12, "R to Reload")

        self.accept("escape", sys.exit, [0])
        self.accept("r", self.reloadTextures)

    def reloadTextures(self):
        pool = TexturePool.findAllTextures()
        for texture in pool:
            print("Reloading " + str(texture))
            texture.reload()
            
        
t = TexturePView()
t.run()
