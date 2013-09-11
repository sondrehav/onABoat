# coding:UTF-8
import pygame, sys, math
from pygame.locals import *
from application import *
from vector import Vector

class Entity(object):
    def __init__(self):
        self.pos = Vector(0,0)
        self.vel = Vector(0,0)
        self.acc = Vector(0,0)
        self.direction = 0
        self.acceleration = 0.1
        self.friction = 0.9 * self.acceleration
        self.maxSpeed = 8
        self.renderCount = 0
        self.ticksBeforeAnimSwitch = 4
        self.shouldAnimate = True
        
        if self.imageNames == None:
            self.imageNames = ["res/defaultimage.png"]

        self.surfaceObjects = []
        for image in self.imageNames:
            self.surfaceObjects.append(pygame.image.load(image))
        self.width = self.surfaceObjects[0].get_width()
        self.height = self.surfaceObjects[0].get_height() 

    def event(self, event):
        self.pos = self.pos + self.vel
        if (self.vel+self.acc).getLengthSqrd() <= self.maxSpeed**2:
            self.vel += self.acc
        else:
            self.vel.setLength(self.maxSpeed)


    def render(self, surface, xpos, ypos, drawVector=False):
        nOfImages = len(self.surfaceObjects)
        index = int((self.renderCount)/self.ticksBeforeAnimSwitch%nOfImages)
        surface.blit(self.surfaceObjects[index], (xpos, ypos))
        if self.shouldAnimate:
            self.renderCount += 1

