import pygame, sys
from pygame.locals import *
from entity import Entity
from vector import *
from random import random, randint
from globals import *

class Bubble(Entity):
    def __init__(self, front=False):
        if front:
            self.imageNames = ["res/bubble.png"]
        else:
            self.imageNames = ["res/bubble_small.png"]
        super(Bubble, self).__init__()

        self.pos = Vector(randint(0,getWidth()), randint(0, getHeight()))
        self.front = front

    def event(self, event):
        super(Bubble, self).event(event)
        if self.pos.x < -16:
            self.pos.x = getWidth()
            self.pos.y = randint(0,getHeight())
        if self.pos.x > getWidth():
            self.pos.x = -16
            self.pos.y = randint(0,getHeight())
        if self.pos.y < -16:
            self.pos.y = getHeight()
            self.pos.x = randint(0,getWidth())
        if self.pos.y > getHeight():
            self.pos.y = -16
            self.pos.x = randint(0,getWidth())

