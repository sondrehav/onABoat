import pygame, sys
from pygame.locals import *
from entity import Entity
from vector import *
from random import random, randint
from globals import *

class Bubble(Entity):
    def __init__(self, front):
        if front:
            self.imageNames = ["res/bubble.png"]
        else:
            self.imageNames = ["res/bubble_small.png"]
        super(Bubble, self).__init__()
        self.xPos = randint(0,getWidth())
        self.yPos = randint(0,getHeight())
        if front:
            self.dirVector.setX(random())
            self.dirVector.setY(-random())
        else:
            self.dirVector.setX(random()/2)
            self.dirVector.setY(-random()/2)

    def event(self, event):
        super(Bubble, self).event(event)
        if self.xPos < -16:
            self.xPos = getWidth()
            self.yPos = randint(0,getHeight())
        if self.xPos > getWidth():
            self.xPos = -16
            self.yPos = randint(0,getHeight())
        if self.yPos < -16:
            self.yPos = getHeight()
            self.xPos = randint(0,getWidth())
        if self.yPos > getHeight():
            self.yPos = -16
            self.xPos = randint(0,getWidth())
