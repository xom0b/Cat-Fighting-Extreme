import pygame
from pygame.locals import *
import sys
import time
import pyganim

pygame.init()

LEFT = 'left'
RIGHT = 'right'

WINDOWWIDTH = 1280
WINDOWHEIGHT = 960
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('temp')

standRightAnim = pyganim.PygAnimation([('testimages/whiteCatF1200.png',0.2),
                                  ('testimages/whiteCatF2200.png',0.2),
                                  ('testimages/whiteCatF3200.png',0.2)])

standLeftAnim = pyganim.PygAnimation([('testimages/whiteCatLeftF1200.png',0.2),
                                      ('testimages/whiteCatLeftF2200.png',0.2),
                                      ('testimages/whiteCatLeftF3200.png',0.2)])

walkLeftAnim = pyganim.PygAnimation([('testimages/whiteCatWalkLeftF1200.png',0.08),
                                    ('testimages/whiteCatWalkLeftF2200.png',0.08),
                                    ('testimages/whiteCatWalkLeftF3200.png',0.08),
                                    ('testimages/whiteCatWalkLeftF4200.png',0.08)])

walkRightAnim = pyganim.PygAnimation([('testimages/whiteCatWalkRightF1200.png',0.08),
                                     ('testimages/whiteCatWalkRightF2200.png',0.08),
                                     ('testimages/whiteCatWalkRightF3200.png',0.08),
                                     ('testimages/whiteCatWalkRightF4200.png',0.08)])

walkDownRightAnim = pyganim.PygAnimation([('testimages/trans1.png',0.1),
                                     ('testimages/trans2.png',0.1),
                                     ('testimages/trans3.png',0.1),
                                     ('testimages/trans4.png',0.1),])

walkDownLeftAnim = pyganim.PygAnimation([('testimages/transleft1.png',0.1),
                                     ('testimages/transleft2.png',0.1),
                                     ('testimages/transleft3.png',0.1),
                                     ('testimages/transleft4.png',0.1),])

                                     
                                     



mainClock=pygame.time.Clock()
BGCOLOR = (255,255,255)

xpos = 100
ypos = 200
ground = 500

currentAction = standRightAnim
currentAction.play()
standLeftAnim.blit(windowSurface,(xpos,ground))

yVel = 0
xRate = 15
gravity = 1.7
isJumping = True
jumpRight = False
jumpLeft = False
keyUp = False

faceRight = True
walking = False

while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            xRate = 15
            keyUp = False
            if event.key == K_LEFT:
                walking = True
                if isJumping:
                    jumpLeft = True
                    currentAction.stop()
                    currentAction = walkDownLeftAnim
                    currentAction.play()
                    faceRight = False

                else:
                    
                    currentAction.stop()
                    currentAction = walkDownLeftAnim
                    currentAction.play()
                    faceRight = False
            elif event.key == K_RIGHT:
                walking = True
                if isJumping:
                    jumpRight = True
                    currentAction.stop()
                    currentAction = walkDownRightAnim
                    currentAction.play()
                    faceRight = True

                else:   
                    
                    currentAction.stop()
                    currentAction = walkDownRightAnim
                    currentAction.play()
                    faceRight = True
            elif event.key == K_UP:
                if isJumping == False:
                    yVel -=25
                    isJumping = True
                
        elif event.type == KEYUP:
            
            if event.key == K_LEFT:
                walking = False
                keyUp = True
   
            elif event.key == K_RIGHT:
                walking = False
                keyUp = True

    if keyUp:
        xRate = 8
        
    if walking == True or isJumping:
        if walking == True:
            if faceRight == True:
                xpos+=xRate
                walkDownRightAnim.blit(windowSurface,(xpos,ypos))
                
            elif faceRight == False:
                xpos-=xRate
                walkDownLeftAnim.blit(windowSurface, (xpos,ypos))
        else:
            if faceRight == True and keyUp:
                xpos+=xRate
                walkDownRightAnim.blit(windowSurface,(xpos,ypos))

            elif faceRight == False and keyUp:
                xpos-=xRate
                walkDownLeftAnim.blit(windowSurface, (xpos,ypos))
            else:
                if faceRight:
                    walkDownRightAnim.blit(windowSurface,(xpos,ypos))
                elif faceRight == False:
                    walkDownLeftAnim.blit(windowSurface,(xpos,ypos))
            
            
    elif walking == False and isJumping == False:
        if faceRight == False:
            walking = False
            currentAction.stop()
            currentAction = standLeftAnim
            currentAction.play()
        else:
            walking == False
            currentAction.stop()
            currentAction = standRightAnim
            currentAction.play()
            
        currentAction.blit(windowSurface, (xpos,ypos))

    #if jumpLeft:
    #    xpos-=15
    #elif jumpRight:
    #    xpos+=15

    if isJumping:
        currentAction.blit(windowSurface, (xpos,ypos))
        yVel+=gravity
        ypos+=yVel
        if ypos > ground:
            ypos = ground
            yVel = 0
            isJumping = False
            jumpLeft = False
            jumpRight = False

            
        
            
    
    pygame.display.update()
    mainClock.tick(30)
