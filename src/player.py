import pygame, sys, math
from collections import deque
from pygame.locals import *
from entity import Entity
from bullet import Bullet
from bubble import Bubble
from vector import *

class Player(Entity):
    def __init__(self):
        self.imageName = "res/submarine.png"
        super(Player, self).__init__()
        self.k_up = False
        self.k_down = False
        self.xPos = 90
        self.bulletList = deque([])
        self.k_r = False
        self.k_l = False
        self.xSpeed = 0
        self.xfriction = 0.995
        self.maxSpeedX = 4
        self.yFrame = 20

    def xMove(self):

        if self.k_r and (math.fabs(self.xSpeed) < self.maxSpeedX):
            self.xSpeed += self.acceleration / 8
            
        if self.k_l and (self.xSpeed > 0):
            self.xSpeed -= self.acceleration / 8
            
        if self.k_r == False and self.k_l == False and self.maxSpeedX != 0:
            self.xSpeed *= self.xfriction
            if math.fabs(self.xSpeed) == self.acceleration:
                self.xSpeed = 0
        
    def movement(self, event):
        if self.k_up and (math.fabs(self.dirVector.getY()) < self.maxSpeed or self.dirVector.getY() > 0):
            self.dirVector.setY(self.dirVector.getY() - self.acceleration)

        if self.k_down and (math.fabs(self.dirVector.getY()) < self.maxSpeed or self.dirVector.getY() < 0):
            self.dirVector.setY(self.dirVector.getY() + self.acceleration)

        if self.k_up == False and self.k_down == False and self.dirVector.getY() != 0:
            self.dirVector.setY(self.dirVector.getY() * self.friction)
            if math.fabs(self.dirVector.getY()) == math.fabs(self.acceleration):
                self.dirVector.setLength(0) 

        for i in range(0, len(self.bulletList)):
            self.bulletList[i].event(event)
            if self.bulletList[i].outOfRange():
                self.bulletList.pop()
                print('gone')
    
    def key(self, event):
        for evt in event:
            if evt.type == KEYDOWN:
                if evt.key == K_UP:
                    self.k_up = True
                if evt.key == K_DOWN:
                    self.k_down = True
                if evt.key == K_SPACE:
                    self.bulletList.append(Bullet(self.xPos + 93,self.yPos + 97))
                if evt.key == K_RIGHT:
                    self.k_r = True
                if evt.key == K_LEFT:
                    self.k_l = True
            elif evt.type == KEYUP:
                if evt.key == K_UP:
                    self.k_up = False
                if evt.key == K_DOWN:
                    self.k_down = False
                if evt.key == K_RIGHT:
                    self.k_r = False
                if evt.key == K_LEFT:
                    self.k_l = False

    def event(self, event):
        self.key(event)
        self.movement(event)
        self.xMove()                       
        super(Player, self).event(event)

    def render(self, surface, drawVector=False):
        for i in range(0, len(self.bulletList)):
            self.bulletList[i].render(surface, drawVector)
        super(Player, self).render(surface, drawVector)
        
    def getXSpeed(self):
        return self.xSpeed