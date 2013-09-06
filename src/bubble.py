import pygame, sys
from pygame.locals import *
from entity import Entity
from vector import *
from random import randint
from globals import *

class Bubble(Entity):
    def __init__(self, front):
        if front:
            self.imageName = "res/bubble.png"
        else:
            self.imageName = "res/bubble_small.png"
        super(Bubble, self).__init__()
        self.xPos = randint(0,getWidth())
        self.yPos = randint(0,getHeight())
        if front:
            self.dirVector.setX(-randint(1,5) * 1.5 / 5)
        else:
            self.dirVector.setX(-randint(1,5) / 5)

    def event(self, event):
        super(Bubble, self).event(event)
        if self.xPos < -16:
            self.xPos = getWidth()
        if self.xPos > getWidth():
            self.xPos = -16
        if self.yPos < -16:
            self.yPos = getHeight()
        if self.yPos > getHeight():
            self.yPos = -16

