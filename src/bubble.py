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
        self.front = front
        if front:
            self.xSpeed = (random() - 0.5)
            self.dirVector.setY(random() - 0.5)
        else:
            self.xSpeed = (random() - 0.5) / 2
            self.dirVector.setY(random() / 2 - 0.25)

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

    def setXSpeedFromPlayer(self, input):
        if self.front:
            self.dirVector.setX(self.xSpeed + input)
        else:
            self.dirVector.setX(self.xSpeed + input / 2)