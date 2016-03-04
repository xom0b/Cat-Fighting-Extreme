#main_0.1
import pygame
from pygame.locals import *
import sys
import time
import pyganim
import catClass
from catClass import*
import fxClass
from fxClass import*

pygame.init()

def main():

    WINDOWWIDTH = 1280
    WINDOWHEIGHT = 960

    W_half = int(WINDOWWIDTH*.5)
    H_half = int(WINDOWHEIGHT*.5)

    ground = H_half

    mainClock=pygame.time.Clock()

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    DKRED = (155,0,0)
    
    BGCOLOR = DKRED

    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Cat Fighting Extreme')

    cat1 = cat(100, int(W_half*1.5), ground, '1' ,[('testimages/whiteCatF1200.png',0.2),
                                                  ('testimages/whiteCatF2200.png',0.2),
                                                  ('testimages/whiteCatF3200.png',0.2),
                                                  ('testimages/whiteCatLeftF1200.png',0.2),
                                                  ('testimages/whiteCatLeftF2200.png',0.2),
                                                  ('testimages/whiteCatLeftF3200.png',0.2),
                                                  ('testimages/trans1.png',0.1),
                                                  ('testimages/trans2.png',0.1),
                                                  ('testimages/trans3.png',0.1),
                                                  ('testimages/trans4.png',0.1),
                                                  ('testimages/transleft1.png',0.1),
                                                  ('testimages/transleft2.png',0.1),
                                                  ('testimages/transleft3.png',0.1),
                                                  ('testimages/transleft4.png',0.1),
                                                  ('images/punch/punch2right.png',0.2),
                                                  ('images/punch/punch2left.png',0.2)])

    jumpDust = fx(int(W_half*1.5), ground, [('images/fx/fx_jumpDust_1.png', 0.07),
                                            ('images/fx/fx_jumpDust_2.png', 0.07),
                                            ('images/fx/fx_jumpDust_3.png', 0.07),
                                            ('images/fx/fx_jumpDust_4.png', 0.07),
                                            ('images/fx/fx_jumpDust_5.png', 0.07),
                                            ('images/fx/fx_jumpDust_6.png', 0.07),], False)
                                            
    

    move = False
    faceRight = True
    
    
    L_DOWN = False
    R_DOWN = False
    
    #Gravity/Jumping Physics constants
    yVel = 0
    xRate = 15
    gravity = 1.7
    
    punch = False
    stand = False
    
    isJumping = False
    keyUp = False

    print(cat1.getX(), cat1.getY())

    cat1.setY(ground)
    fallSpot = (cat1.getX(),cat1.getY())
    
    while True:

        windowSurface.fill(BGCOLOR)
        landed = False
            
        for event in pygame.event.get():

            #Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #Keydown
            elif event.type == KEYDOWN:

                keyUp = False

                if event.key == K_UP:
                    if isJumping == False:

                        isJumping = True
                        yVel -= 25

                if event.key == K_LEFT:
                    print('LEFT')
                    move = True
                    L_DOWN = True
                    faceRight = False
                    
                    
                if event.key == K_RIGHT:
                    print('RIGHT')
                    move = True
                    R_DOWN = True
                    faceRight = True
                    
                if event.key == K_n:
                    print("punch")
                    punch = True
                    

            #Keyup
            elif event.type == KEYUP:

                if event.key==K_LEFT:
                    L_DOWN = False
                    keyUp = True
                    #only sets move to 'False' if both movement keys are being held down
                    if R_DOWN == False and isJumping == False:
                        move = False


                    
                if event.key==K_RIGHT:
                    R_DOWN = False
                    keyUp = True
                    #only sets move to 'False' if both movement keys are being held down
                    if L_DOWN == False and isJumping == False:
                        move = False



        

        #WALKING        
        if move and isJumping == False:
            if faceRight:
                cat1.moving('right', 15)
                cat1.setAction('walkRight')
            else:
                cat1.moving('left', 15)
                cat1.setAction('walkLeft')


                

        #STANDING
        else:
            if faceRight:
                cat1.setAction('standRight')
            else:
                cat1.setAction('standLeft')


        
        #JUMPING
        if isJumping:

            #animations while jumping
            if faceRight and R_DOWN:
                cat1.moving('right', 15)
                cat1.setAction('walkRight')
                
            elif faceRight == False and L_DOWN:
                cat1.moving('left', 15)
                cat1.setAction('walkLeft')

            elif faceRight and keyUp:
                cat1.moving('right', 8)
                cat1.setAction('walkRight')
            elif faceRight == False and keyUp:
                cat1.moving('left', 8)
                cat1.setAction('walkLeft')
                
            #sets ypos
            yVel+=gravity
            cat1.setY(cat1.getY()+yVel)

            #checks if the cat has landed on the ground or not
            if cat1.getY() > ground:
                
                

                #Dust for when you land is set to play when you land at the spot (fallSpot) you landed
                jumpDust.getAnim().play()
                fallSpot = (cat1.getX(),cat1.getY())
                
                
                yVel = 0
                isJumping = False
                if keyUp:
                    move = False

        if punch:
            if faceRight:
                cat1.setAction('punchRight')
            else:
                cat1.setAction('punchLeft')


        cat1.getAction().play()
        cat1.getAction().blit(windowSurface, (cat1.getX(), cat1.getY()))
        
        jumpDust.getAnim().blit(windowSurface, fallSpot)
        



        pygame.display.update()
        mainClock.tick(30)
        
        
    


if __name__ == '__main__': main()
