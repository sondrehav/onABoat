import pygame, sys
from pygame.locals import *
from entity import Entity
from vector import *

class Bullet(Entity):
    def __init__(self, x, y):
        self.imageName = "res/ammo.png"
        super(Bullet, self).__init__()
        self.xPos = x
        self.yPos = y
        self.dirVector.setX(10)
    def event(self, event):
        super(Bullet, self).event(event)
        #if self.xPos > 640:
            #self.__del__()
        
    def outOfRange(self):
        if self.xPos > 640:
            return True
