import pygame, sys, math
from pygame.locals import *
from entity import Entity
from vector import *

class Player(Entity):
    def __init__(self):
        self.imageName = "submarine.png"
        super(Player, self).__init__()
        self.k_up = False
        self.k_down = False
    def event(self, event):
        for evt in event:
            if evt.type == KEYDOWN:
                if evt.key == K_UP:
                    self.k_up = True
                if evt.key == K_DOWN:
                    self.k_down = True
            elif evt.type == KEYUP:
                if evt.key == K_UP:
                    self.k_up = False
                if evt.key == K_DOWN:
                    self.k_down = False
        
        if self.k_up == True and self.dirVector.getLength() < self.maxSpeed:
            self.dirVector.setY(self.dirVector.getY() - self.acceleration)
        if self.k_down == True and self.dirVector.getLength() < self.maxSpeed:
            self.dirVector.setY(self.dirVector.getY() + self.acceleration)
        if self.k_up == False and self.k_down == False and self.dirVector.getLength() != 0:
            self.dirVector.setLength(self.dirVector.getLength() * self.friction)
            if self.dirVector.getLength() == math.fabs(self.acceleration):
                self.dirVector.setLength(0)
        
        super(Player, self).event(event)
    def render(self, surface):
        super(Player, self).render(surface)
    
