import pygame, sys
from pygame.locals import *
from entity import Entity
from vector import *
from globals import *

class Bullet2(Entity):
    def __init__(self, x, y):
        self.imageNames = ["res/ammo2.png"]
        super(Bullet2, self).__init__()
        self.xPos = x
        self.yPos = y
        
    def outOfRange(self):
        if self.xPos > getWidth():
            return True

    def speed(self, input):
        self.dirVector.setX(12 - input)
        
    def render(self, surface, drawVector = False):
        surface.blit(self.surfaceObjects[0], (self.xPos, self.yPos))
        super(Bullet2, self).render(surface, drawVector)