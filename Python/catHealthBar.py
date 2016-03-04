#catLifeBox.py

#import pyganim
import pygame
from pygame.locals import *
class catHealthBar:
    def __init__(self,health,xpos,ypos,color,surf,width,height):
        self.XPOS=xpos
        self.YPOS=ypos
        self.HEALTH=health
        self.COLOR=color
        self.SURF=surf
        self.WIDTH=width
        self.OVERALL_WIDTH = width
        self.HEIGHT=height
        self.HEALTHBARSURF=pygame.Surface((self.WIDTH,self.HEIGHT),flags=SRCALPHA,depth=32)

       #pygame.draw.rect(self.HEALTHBARSURF, self.COLOR,  Rect((self.XPOS,self.YPOS),(self.WIDTH,self.HEIGHT)))



    def displayHealthBar(self):
        #self.loseHealth()
        self.HEALTHBARSURF.fill(self.COLOR)

        #self.HEALTHBARSURF.fill((255,100,100))

        pygame.draw.rect(self.HEALTHBARSURF,(255,0,0),  Rect((0,0),(self.WIDTH,self.HEIGHT),width=1))

        self.SURF.blit(self.HEALTHBARSURF,(self.XPOS,self.YPOS))

    def loseHealth(self):

        if(self.WIDTH>0):
            self.WIDTH=self.WIDTH - self.OVERALL_WIDTH//10
        self.HEALTHBARSURF=pygame.Surface((self.WIDTH,self.HEIGHT),flags=SRCALPHA,depth=32)







