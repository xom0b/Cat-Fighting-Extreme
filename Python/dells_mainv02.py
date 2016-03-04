#main_0.2
import pygame
from pygame.locals import *
import sys
import time
import pyganim
import catClass
from catClass import*
import fxClass
from fxClass import*
import Collision
from Collision import *


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

    LEFT = 'left'
    RIGHT = 'right'

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
                                            ('images/fx/fx_jumpDust_6.png', 0.07)], False)

    bluePunch_right = fx(int(W_half*1.5), ground,[('images/fx/fx_bluepunchright1.png',0.1),
                                                  ('images/fx/fx_bluepunchright2.png',0.1),
                                                  ('images/fx/fx_bluepunchright3.png',0.1),
                                                  ('images/fx/fx_bluepunchright4.png',0.1)], False)

    bluePunch_left = fx(int(W_half*1.5), ground,[('images/fx/fx_bluepunchleft1.png',0.1),
                                                 ('images/fx/fx_bluepunchleft2.png',0.1),
                                                 ('images/fx/fx_bluepunchleft3.png',0.1),
                                                 ('images/fx/fx_bluepunchleft4.png',0.1)], False)

    cat1Hit=HitBox(cat1.getX(),cat1.getY(),75,135)
    sprites = pygame.sprite.Group()
    sprites.add(cat1Hit)
    cat2Hit=HitBox(100,480,200,200)
    sprites.add(cat2Hit)
    cat1Punch=HitBox(cat1.getX(),cat1.getY(),55,25)





    ###Keypress booleans

    #Player 1
    up_down = False
    right_down = False
    left_down = False

    punch1_down = False
    block1_down = False

    walking1 = False
    jumping1 = False
    punching1 = False
    blocking1 = False
    standjump1 = False

    keyup1 = False

    punching1_finished = False
    blocking1_finished = False

    #Player 2
    w_down = False
    a_down = False
    d_down = False

    punch2_down = False
    block2_down = False

    walking2 = False
    jumping2 = False
    punching2 = False
    blocking2 = False
    standjump2 = False

    keyup2 = False

    punching2_finished = False
    blocking2_finished = False

    #Gravity/Jumping Physics constants
    p1_yVel = 0
    p1_xRate = 15
    p1_gravity = 1.7

    p2_yVel = 0
    p2_xRate = 15
    p2_gravity = 1.7

    #Players Directions
    cat1_direction = LEFT
    cat2_direction = RIGHT




    cat1.setY(ground)
    fallSpot = (cat1.getX(),cat1.getY())
    punchSpot = (cat1.getX(), cat1.getY())

    while True:

        windowSurface.fill(BGCOLOR)

        for event in pygame.event.get():

            #Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #Keydown
            elif event.type == KEYDOWN:

                if event.key == K_UP:
                    up_down = True
                if event.key == K_RIGHT:
                    right_down = True
                    left_down = False
                    keyup1 = False
                if event.key == K_LEFT:
                    left_down = True
                    right_down = False
                    keyup1 = False
                if event.key == K_COMMA:
                    punch1_down = True
                    block1_down = False
                if event.key == K_PERIOD:
                    block1_down = True
                    punch1_down = False

            elif event.type == KEYUP:

                if event.key == K_UP:
                    up_down = False
                if event.key == K_RIGHT:
                    right_down = False
                    keyup1 = True
                if event.key == K_LEFT:
                    left_down = False
                    keyup1 = True
                if event.key == K_COMMA:
                    punch1_down = False
                if event.key == K_PERIOD:
                    block1_down = False


        ###Moves p1 X & Y based off booleans

        #p1 ground movement right
        if right_down:
            cat1.moving('right', 15)
            cat1_direction = RIGHT
            if jumping1 == False:
                walking1 = True


        #p1 ground movement left
        if left_down:
            cat1.moving('left', 15)
            cat1_direction = LEFT
            if jumping1 == False:
                walking1 = True

        if cat1.getY() == ground:
            keyup1 = False

        if right_down == False and left_down == False:
            walking1 = False



        #p1 jumping boolean change
        if up_down and jumping1 == False:
            jumping1 = True
            p1_yVel = -25



        #p1 jumping nonsense
        if jumping1:

            if cat1_direction == RIGHT and keyup1:
                cat1.moving('right', 8)

            if cat1_direction == LEFT and keyup1:
                cat1.moving('left', 8)

            p1_yVel+=p1_gravity
            cat1.setY(cat1.getY()+p1_yVel)

            if cat1.getY() > ground:

                keyup1 = False
                p1_yVel = 0
                jumping1 = False


                #Plays particle effect for landing
                jumpDust.getAnim().play()
                fallSpot = (cat1.getX(),cat1.getY())

        ###Sets animations based off key presses

        if punch1_down:

            punchSpot = (cat1.getX(), cat1.getY())

            if cat1_direction == RIGHT:
                cat1.setAction("punchRight")
                bluePunch_right.getAnim().play()


            else:
                cat1.setAction("punchLeft")
                bluePunch_left.getAnim().play()
                #adds the cat1 punch
                sprites.add(cat1Punch)
                punch1_down= False



        elif walking1 or jumping1:

            if cat1_direction == RIGHT:
                cat1.setAction("walkRight")
            else:
                cat1.setAction("walkLeft")

        else:
            sprites.remove(cat1Punch)
            if cat1_direction == RIGHT:
                cat1.setAction("standRight")
            else:
                cat1.setAction("standLeft")


        cat1.getAction().play()
        cat1.getAction().blit(windowSurface, (cat1.getX(), cat1.getY()))

        jumpDust.getAnim().blit(windowSurface, fallSpot)

        bluePunch_right.getAnim().blit(windowSurface, punchSpot)
        bluePunch_left.getAnim().blit(windowSurface, punchSpot)

        #cat 2 stuff unfinished
        cat2Hit.rect.x = 100
        cat2Hit.rect.y = 480

        #places the punching hit box for punching left

        cat1Punch.rect.x = cat1.getX()+30
        cat1Punch.rect.y = cat1.getY()+ 100

        #places the hitbox for the cat
        cat1Hit.rect.x = cat1.getX() +65
        cat1Hit.rect.y = cat1.getY() +30

        sprites.draw(windowSurface)
        if punch1_down is True:

            cat1Col=pygame.sprite.collide_rect(cat1Punch,cat2Hit)

            print(cat1Col)
            if cat1Col == 1:

                cat1.isHit()
                print(cat1.getHealth())
                cat1Col= False


        pygame.display.update()
        mainClock.tick(30)




if __name__ == '__main__': main()