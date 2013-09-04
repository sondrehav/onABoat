import pygame, sys, math
from pygame.locals import *
from application import *
from vector import *

class Entity(object):
    def __init__(self):
        self.xPos = 10
        self.yPos = 50
        if self.imageName == None:
            self.imageName = "defaultimage.png"
        self.dirVector = Vector(0,0)
        self.velocity = 0
        self.direction = 0
        self.acceleration = 0.25
        self.friction = 0.125
        self.maxSpeed = 8
        
        self.surfaceObject = pygame.image.load(self.imageName)
        self.width = self.surfaceObject.get_width()
        self.height = self.surfaceObject.get_height() 
    def event(self, event):
        self.xPos += self.dirVector.getX()
        self.yPos += self.dirVector.getY()
    def render(self, surface):
        surface.blit(self.surfaceObject, (self.xPos,self.yPos))