#catClass.py

import pyganim

class cat:

    def __init__(self, health, xpos, ypos, playerNum, sprites):

        self.HEALTH = health

        self.XPOS = xpos
        self.YPOS = ypos

        self.standRight = pyganim.PygAnimation(sprites[0:3])
        self.standLeft = pyganim.PygAnimation(sprites[3:6])
        self.walkRight = pyganim.PygAnimation(sprites[6:10])
        self.walkLeft = pyganim.PygAnimation(sprites[10:14])
        self.punchRight = pyganim.PygAnimation(sprites[14:15], False)
        self.punchLeft = pyganim.PygAnimation(sprites[15:16], False)
        
        if playerNum == '1':
            self.currentAction = self.standLeft
        elif playerNum == '2':
            self.currentAction = self.standRight
        

    def getX(self):
        
        return self.XPOS

    def getY(self):

        return self.YPOS

    def setX(self, x):

        self.XPOS = x

    def setY(self, y):

        self.YPOS = y

    def getHealth(self):

        return self.HEALTH

    def getAction(self):

        return self.currentAction

    def isHit(self):

        self.HEALTH -= 10

    def setAction(self, action):

        if action == 'walkRight':
            self.currentAction = self.walkRight
        elif action == 'walkLeft':
            self.currentAction = self.walkLeft
        elif action == 'standRight':
            self.currentAction = self.standRight
        elif action == 'standLeft':
            self.currentAction = self.standLeft
        elif action == 'punchRight':
            self.currentAction = self.punchRight
        elif action == 'punchLeft':
            self.currentAction = self.punchLeft

            
    def moving (self, direction, rate):
        if direction == 'right':
            self.XPOS += rate
        elif direction == 'left':
            self.XPOS -= rate
            

        
            

        
            
            

        
