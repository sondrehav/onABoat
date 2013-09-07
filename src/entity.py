# coding:UTF-8
import pygame, sys, math
from pygame.locals import *
from application import *
from vector import *

class Entity(object):
    def __init__(self):
        self.xPos = 10
        self.yPos = 50
        if self.imageNames == None:
            self.imageNames = ["res/defaultimage.png"]
        self.dirVector = Vector(0,0)
        self.velocity = 0
        self.direction = 0
        self.acceleration = 0.25
        self.friction = 0.9
        self.maxSpeed = 8
        self.renderCount = 0
        self.ticksBeforeAnimSwitch = 4
        
        self.surfaceObjects = []
        for image in self.imageNames:
            self.surfaceObjects.append(pygame.image.load(image))
        self.surfaceObject = self.surfaceObjects[0] #for å ikke ødelegge annen kode. 
        self.width = self.surfaceObject.get_width()
        self.height = self.surfaceObject.get_height() 

    def event(self, event):
        self.xPos += self.dirVector.getX()
        self.yPos += self.dirVector.getY()
        self.dirVector.xPos = self.xPos + self.width/2
        self.dirVector.yPos= self.yPos + self.height/2

    def render(self, surface, drawVector=False):
        surface.blit(self.surfaceObjects[int((self.renderCount)/self.ticksBeforeAnimSwitch%len(self.imageNames))], (self.xPos,self.yPos))
        self.renderCount += 1
        if drawVector:
            self.dirVector.render(surface)
