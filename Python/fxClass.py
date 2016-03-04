#fxClass.py

import pyganim

class fx:

    def __init__(self, xpos, ypos, sprites, loop):

        self.XPOS = xpos
        self.YPOS = ypos

        self.ANIM = pyganim.PygAnimation(sprites, loop)

    def getAnim(self):

        return self.ANIM

    def getX(self):

        return self.XPOS

    def getY(self):

        return self.YPOS

    def setX(self, x):

        self.XPOS = x

    def setY(self, y):

        self.YPOS = y
        
