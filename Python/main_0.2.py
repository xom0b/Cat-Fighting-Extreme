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
from Collision import*
import catHealthBar
from catHealthBar import*



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

    cat1_health = catHealthBar(100,WINDOWHEIGHT - WINDOWHEIGHT//5,WINDOWHEIGHT//8, BLACK, windowSurface, 400, 100)
    cat2_health = catHealthBar(100,WINDOWHEIGHT//10,WINDOWHEIGHT//8, BLACK, windowSurface, 400, 100)



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


    cat2 = cat(100,int(W_half*1.5//4),ground,'2',[('Negatestimages/negativeCatF1200.fw.png',0.2),
                                             ('Negatestimages/negativeCatF2200.fw.png',0.2),
                                                       ('Negatestimages/negativeCatF3200.fw.png',0.2),
                                                  ('Negatestimages/negativeCatLeftF1200.fw.png',0.2),
                                                  ('Negatestimages/negativeCatLeftF2200.fw.png',0.2),
                                                  ('Negatestimages/negativeCatLeftF3200.fw.png',0.2),
                                                  ('Negatestimages/negativetrans1.fw.png',0.1),
                                                  ('Negatestimages/negativetrans2.fw.png',0.1),
                                                  ('Negatestimages/negativetrans3.fw.png',0.1),
                                                  ('Negatestimages/negativetrans4.fw.png',0.1),
                                                  ('Negatestimages/negativetransleft1.fw.png',0.1),
                                                  ('Negatestimages/negativetransleft2.fw.png',0.1),
                                                  ('Negatestimages/negativetransleft3.fw.png',0.1),
                                                  ('Negatestimages/negativetransleft4.fw.png',0.1),
                                                  ('images/punch/negativepunch2right.fw.png',0.2),
                                                  ('images/punch/negativepunch2left.fw.png',0.2)])



    #NORMAL CAT SHIT

    jumpDust = fx(int(W_half*1.5), ground, [('images/fx/fx_jumpDust_1.png', 0.07),
                                            ('images/fx/fx_jumpDust_2.png', 0.07),
                                            ('images/fx/fx_jumpDust_3.png', 0.07),
                                            ('images/fx/fx_jumpDust_4.png', 0.07),
                                            ('images/fx/fx_jumpDust_5.png', 0.07),
                                            ('images/fx/fx_jumpDust_6.png', 0.07)], False)

    bluePunch_right = fx(int(W_half*1.5), ground,[('images/fx/punch3.1.png',0.05),
                                                  ('images/fx/punch3.2.png',0.05),
                                                  ('images/fx/punch3.3.png',0.05),
                                                  ('images/fx/punch3.4.png',0.05)], False)

    bluePunch_left = fx(int(W_half*1.5), ground,[('images/fx/punchleft3.1.png',0.05),
                                                 ('images/fx/punchleft3.2.png',0.05),
                                                 ('images/fx/punchleft3.3.png',0.05),
                                                 ('images/fx/punchleft3.4.png',0.05)], False)

    blueBlock_right = fx(int(W_half*1.5), ground, [('images/block/blueBlock_right1.png', 0.05),
                                                   ('images/block/blueBlock_right2.png', 0.05),
                                                   ('images/block/blueBlock_right3.png', 0.05)], False)

    blueBlock_left = fx(int(W_half*1.5), ground, [('images/block/blueBlock_left1.png', 0.05),
                                                  ('images/block/blueBlock_left2.png', 0.05),
                                                  ('images/block/blueBlock_left3.png', 0.05)], False)
    #NEGA CAT SHIT

    negajumpDust = fx(int(W_half*1.5), ground, [('images/fx/fx_jumpDust_1.png', 0.07),
                                            ('images/fx/fx_jumpDust_2.png', 0.07),
                                            ('images/fx/fx_jumpDust_3.png', 0.07),
                                            ('images/fx/fx_jumpDust_4.png', 0.07),
                                            ('images/fx/fx_jumpDust_5.png', 0.07),
                                            ('images/fx/fx_jumpDust_6.png', 0.07)], False)

    negabluePunch_right = fx(int(W_half*1.5), ground,[('images/fx/punch3.1.png',0.05),
                                                  ('images/fx/punch3.2.png',0.05),
                                                  ('images/fx/punch3.3.png',0.05),
                                                  ('images/fx/punch3.4.png',0.05)], False)

    negabluePunch_left = fx(int(W_half*1.5), ground,[('images/fx/punchleft3.1.png',0.05),
                                                 ('images/fx/punchleft3.2.png',0.05),
                                                 ('images/fx/punchleft3.3.png',0.05),
                                                 ('images/fx/punchleft3.4.png',0.05)], False)

    negablueBlock_right = fx(int(W_half*1.5), ground, [('images/block/blueBlock_right1.png', 0.05),
                                                   ('images/block/blueBlock_right2.png', 0.05),
                                                   ('images/block/blueBlock_right3.png', 0.05)], False)

    negablueBlock_left = fx(int(W_half*1.5), ground, [('images/block/blueBlock_left1.png', 0.05),
                                                  ('images/block/blueBlock_left2.png', 0.05),
                                                  ('images/block/blueBlock_left3.png', 0.05)], False)



    sprites = pygame.sprite.Group()

    cat1Hit=HitBox(cat1.getX(),cat1.getY(),75,135)
    sprites.add(cat1Hit)

    cat1Punch=HitBox(cat1.getX(),cat1.getY(),55,25)
    sprites.add(cat1Punch)

    cat2Hit=HitBox(cat1.getX(),cat1.getY(),75,135)
    sprites.add(cat2Hit)

    cat2Punch=HitBox(cat1.getX(),cat1.getY(),55,25)
    sprites.add(cat2Punch)





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
    cat1_blockSpot = (cat1.getX(), cat1.getY())

    cat2.setY(ground)
    negafallSpot=(cat2.getX(),cat2.getY())
    negapunchSpot=(cat2.getX(),cat2.getY())
    cat2_blockSpot=(cat2.getX(),cat2.getY())

    while True:

        windowSurface.fill(BGCOLOR)

        for event in pygame.event.get():

            #Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #Keydown
            elif event.type == KEYDOWN:

                #Player 1

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

                #Player 2

                if event.key == K_w:
                    w_down = True
                if event.key == K_d:
                    d_down = True
                    a_down = False
                    keyup2 = False
                if event.key == K_a:
                    a_down = True
                    d_down = False
                    keyup2 = False
                if event.key == K_c:
                    punch2_down = True
                    block2_down = False
                if event.key == K_v:
                    block2_down = True
                    punch2_down = False

            elif event.type == KEYUP:

                #Player 1

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

                #Player 2

                if event.key == K_w:
                    w_down = False
                if event.key == K_d:
                    d_down= False
                    keyup2 = True
                if event.key == K_a:
                    a_down = False
                    keyup2 = True
                if event.key == K_c:
                    punch2_down = False
                if event.key == K_v:
                    block2_down = False


        ###Moves p1 X & Y based off booleans

        #p1 ground movement right
        if right_down:
            cat1.moving('right', 15)
            cat1_direction = RIGHT
            if jumping1 == False:
                walking1 = True

        #p2 ground movement right
        if d_down:
            cat2.moving('right',15)
            cat2_direction=RIGHT
            if jumping2==False:
                walking2 = True


        #p1 ground movement left
        if left_down:
            cat1.moving('left', 15)
            cat1_direction = LEFT
            if jumping1 == False:
                walking1 = True

        #p2 ground movement left
        if a_down:
            cat2.moving('left', 15)
            cat2_direction = LEFT
            if jumping2 == False:
                walking2 = True

        if cat1.getY() == ground:
            keyup1 = False

        if right_down == False and left_down == False:
            walking1 = False

        if cat2.getY() == ground:
            keyup2 = False

        if d_down == False and a_down == False:
            walking2 = False



        #p1 jumping boolean change
        if up_down and jumping1 == False:
            jumping1 = True
            p1_yVel = -25

        #p2 jumping boolean change
        if w_down and jumping2 == False:
            jumping2 = True
            p2_yVel = -25



        #p1 jumping nonsense
        if jumping1:

            if cat1_direction == RIGHT and keyup1:
                cat1.moving('right', 8)

            if cat1_direction == LEFT and keyup1:
                cat1.moving('left', 8)

            p1_yVel+=p1_gravity
            cat1.setY(cat1.getY()+p1_yVel)

            if cat1.getY() > ground:

                cat1.setY(ground)

                keyup1 = False
                p1_yVel = 0
                jumping1 = False


                #Plays particle effect for landing
                jumpDust.getAnim().play()
                fallSpot = (cat1.getX(),cat1.getY())

        if jumping2:

            if cat2_direction == RIGHT and keyup2:
                cat2.moving('right', 8)

            if cat2_direction == LEFT and keyup2:
                cat2.moving('left', 8)

            p2_yVel+=p2_gravity
            cat2.setY(cat2.getY()+p2_yVel)

            if cat2.getY() > ground:

                cat2.setY(ground)

                keyup2 = False
                p2_yVel = 0
                jumping2 = False


                #Plays particle effect for landing
                jumpDust.getAnim().play()
                fallSpot = (cat2.getX(),cat2.getY())

        ###Sets animations based off key presses

        if block1_down:

            if cat1_direction == RIGHT:

                cat1_blockSpot = (cat1.getX(), cat1.getY())
                cat1.setAction("standRight")
                blueBlock_right.getAnim().play()
                if not jumping1:
                    right_down = False

            if cat1_direction == LEFT:

                cat1_blockSpot = (cat1.getX(), cat1.getY())
                cat1.setAction("standLeft")
                blueBlock_left.getAnim().play()
                if not jumping1:
                    left_down = False


        if block2_down:

            if cat2_direction == RIGHT:

                cat2_blockSpot = (cat2.getX(), cat2.getY())
                cat2.setAction("standRight")
                negablueBlock_right.getAnim().play()
                if not jumping2:
                    d_down = False

            if cat2_direction == LEFT:

                cat2_blockSpot = (cat2.getX(), cat2.getY())
                cat2.setAction("standLeft")
                negablueBlock_left.getAnim().play()
                if not jumping2:
                    a_down = False


        if punch1_down and not block1_down:

            if cat1_direction == RIGHT:
                cat1Punch.rect.x = cat1.getX()+ 115
                cat1Punch.rect.y = cat1.getY()+ 100

                cat1.setAction("punchRight")
                bluePunch_right.getAnim().play()
                punchSpot = (cat1.getX()-20, cat1.getY())

                sprites.add(cat1Punch)

            else:
                cat1Punch.rect.x = cat1.getX()+30
                cat1Punch.rect.y = cat1.getY()+ 100

                cat1.setAction("punchLeft")
                bluePunch_left.getAnim().play()
                punchSpot = (cat1.getX()+20, cat1.getY())

                sprites.add(cat1Punch)


        elif walking1 or jumping1 and not block1_down:

            if cat1_direction == RIGHT:
                cat1.setAction("walkRight")
            else:
                cat1.setAction("walkLeft")

        else:

            if cat1_direction == RIGHT:
                cat1.setAction("standRight")
            else:
                cat1.setAction("standLeft")


        if punch2_down and not block2_down:



            if cat2_direction == RIGHT:

                negapunchSpot = (cat2.getX(), cat2.getY())

                cat2Punch.rect.x = cat2.getX()+ 115
                cat2Punch.rect.y = cat2.getY()+ 100

                cat2.setAction("punchRight")
                negabluePunch_right.getAnim().play()


            else:

                negapunchSpot = (cat2.getX(), cat2.getY())

                cat2Punch.rect.x = cat2.getX()+30
                cat2Punch.rect.y = cat2.getY()+ 100

                cat2.setAction("punchLeft")
                negabluePunch_left.getAnim().play()


        elif walking2 or jumping2 and not block2_down:

            if cat2_direction == RIGHT:
                cat2.setAction("walkRight")
            else:
                cat2.setAction("walkLeft")

        else:

            if cat2_direction == RIGHT:
                cat2.setAction("standRight")
            else:
                cat2.setAction("standLeft")


        if cat1.getX() <= 0:
            cat1.setX(0)

        if cat1.getX() >= WINDOWWIDTH-200:
            cat1.setX(WINDOWWIDTH-200)

        if cat2.getX() <= 0:
            cat2.setX(0)

        if cat2.getX() >= WINDOWWIDTH-200:
            cat2.setX(WINDOWWIDTH-200)

        #blits all animations

        cat1.getAction().play()
        cat1.getAction().blit(windowSurface, (cat1.getX(), cat1.getY()))

        cat2.getAction().play()
        cat2.getAction().blit(windowSurface, (cat2.getX(), cat2.getY()))

        jumpDust.getAnim().blit(windowSurface, fallSpot)
        negajumpDust.getAnim().blit(windowSurface, negafallSpot)

        bluePunch_right.getAnim().blit(windowSurface, punchSpot)
        bluePunch_left.getAnim().blit(windowSurface, punchSpot)

        negabluePunch_right.getAnim().blit(windowSurface, negapunchSpot)
        negabluePunch_left.getAnim().blit(windowSurface, negapunchSpot)

        blueBlock_right.getAnim().blit(windowSurface, cat1_blockSpot)
        blueBlock_left.getAnim().blit(windowSurface, cat1_blockSpot)

        negablueBlock_right.getAnim().blit(windowSurface, cat2_blockSpot)
        negablueBlock_left.getAnim().blit(windowSurface, cat2_blockSpot)

        #places the hitbox for the cat
        cat1Hit.rect.x = cat1.getX() +65
        cat1Hit.rect.y = cat1.getY() +30

        cat2Hit.rect.x = cat2.getX() +65
        cat2Hit.rect.y = cat2.getY() +30

        #sprites.draw(windowSurface)

        if pygame.sprite.collide_rect(cat1Punch, cat2Hit) and punch1_down and not block2_down:
            cat2.isHit()
            cat2_health.loseHealth()
            print(cat2.getHealth())

        if pygame.sprite.collide_rect(cat2Punch, cat1Hit) and punch2_down and not block1_down:
            cat1.isHit()
            cat1_health.loseHealth()
            print(cat1.getHealth())

        cat1_health.displayHealthBar()
        cat2_health.displayHealthBar()

        punch1_down = False
        punch2_down = False


        pygame.display.update()
        mainClock.tick(30)




if __name__ == '__main__': main()
