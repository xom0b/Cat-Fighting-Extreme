
import pygame


class HitBox(pygame.sprite.Sprite):

    def __init__(self, posX, posY, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.posX = posX
        self.posY = posY
        self.image = pygame.Surface([width, height])
        self.image.fill((255,255,255))
#        self.image.set_alpha(0)
        self.rect = self.image.get_rect()

    def getRect(self):
        return self.rect