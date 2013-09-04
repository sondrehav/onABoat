import pygame, sys
from pygame.locals import *
from entity import Entity
from vector import *

class Bubble(Entity):
    def __init__(self):
        self.imageName = "bubble.png"
        super(Bubble, self).__init__()
    def event(self):
        super(Bubble, self).event(event)
    def render(self, surface):
        super(Bubble, self).render(surface)