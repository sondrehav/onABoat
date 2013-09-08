import pygame, sys, math
from pygame.locals import *
from entity import Entity
from bullet import Bullet
from bullet2 import Bullet2
from bubble import Bubble
from globals import *
from vector import *

class Player(Entity):
    def __init__(self):
        self.imageNames =["res/submarine1.png","res/submarine2.png","res/submarine3.png","res/submarine2.png"]
        super(Player, self).__init__()
        self.k_up = False
        self.k_down = False
        self.xPos = 40
        self.bulletList = []
        self.bulletList2 = []
        self.k_r = False
        self.k_l = False
        self.xSpeed = 0
        self.xfriction = 0.995
        self.maxSpeedX = 4
        self.yFrame = 20
        self.timer = getFPS() * 5
        self.counter = False
        self.timer2 = getFPS() * 0.1
        self.k_s = False

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

        i = 0
        while i < len(self.bulletList):
            self.bulletList[i].event(event)
            if self.bulletList[i].outOfRange():
                self.bulletList.pop(i)   
                continue
            i+=1
        while i < len(self.bulletList2):
            self.bulletList2[i].event(event)
            if self.bulletList2[i].outOfRange():
                self.bulletList2.pop(i)   
                continue
            i+=1
            
    def key(self, event):
        for evt in event:
            if evt.type == KEYDOWN:
                if evt.key == K_UP:
                    self.k_up = True
                if evt.key == K_DOWN:
                    self.k_down = True
                if evt.key == K_a:
                    if self.counter == False:
                        self.bulletList.append(Bullet(self.xPos + 117,self.yPos + 76))
                        self.counter = True
                if evt.key == K_s:
                    self.k_s = True
                if evt.key == K_RIGHT:
                    self.k_r = True
                if evt.key == K_LEFT:
                    self.k_l = True
            elif evt.type == KEYUP:
                if evt.key == K_UP:
                    self.k_up = False
                if evt.key == K_DOWN:
                    self.k_down = False
                if evt.key == K_s:
                    self.k_s = False
                if evt.key == K_RIGHT:
                    self.k_r = False
                if evt.key == K_LEFT:
                    self.k_l = False

    def event(self, event):
        self.key(event)
        if self.counter == True:
            if self.timer != 0:
                self.timer -= 1
            else:
                self.counter = False
                self.timer = getFPS() * 5
        if self.k_s == True:
            if self.timer2 != 0:
                self.timer2 -= 1
            else:
                self.bulletList2.append(Bullet2(self.xPos + 109,self.yPos + 93))
                self.timer2 = getFPS() * 0.1
            
        self.movement(event)
        self.xMove()
        self.ticksBeforeAnimSwitch = 36 - int(self.getXSpeed()) * 8
        super(Player, self).event(event)
        for i in range(0, len(self.bulletList)):
            self.bulletList[i].speed(self.xSpeed)
        for i in range(0, len(self.bulletList2)):
            self.bulletList2[i].speed(self.xSpeed)

    def render(self, surface, drawVector=False):
        for i in range(0, len(self.bulletList)):
            self.bulletList[i].render(surface, drawVector)
        for i in range(0, len(self.bulletList2)):
            self.bulletList2[i].render(surface, drawVector)
        super(Player, self).render(surface, drawVector)
        
    def getXSpeed(self):
        return self.xSpeed


