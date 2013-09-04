import pygame, sys
from pygame.locals import *
from entity import Entity
from vector import *
from random import randint

class Bubble(Entity):
    def __init__(self, front):
        if front:
            self.imageName = "bubble.png"
        else:
            self.imageName = "bubble_small.png"
        super(Bubble, self).__init__()
        self.xPos = randint(0,640)
        self.yPos = randint(0,480)
        if front:
            self.dirVector.setX(-randint(1,5) * 1.5 / 5)
        else:
            self.dirVector.setX(-randint(1,5) / 5)

    def event(self, event):
        super(Bubble, self).event(event)
        if self.xPos <= -16:
            self.xPos = 640

    def render(self, surface):
        super(Bubble, self).render(surface)
