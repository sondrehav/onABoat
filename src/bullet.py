import pygame, sys
from pygame.locals import *
from entity import Entity
from vector import *
from globals import *

class Bullet(Entity):
    def __init__(self, x, y):
        self.imageNames = ["res/ammo.png"]
        super(Bullet, self).__init__()
        self.xPos = x
        self.yPos = y
        self.dirVector.setX(10)
    def outOfRange(self):
        if self.xPos > getWidth():
            return True