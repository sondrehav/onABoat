import pygame, sys, math
from pygame.locals import *
from entity import Entity
from bullet import Bullet
from bullet2 import Bullet2
from globals import *

class Player(Entity):
    def __init__(self):
        self.imageNames =["res/submarine1.png","res/submarine2.png","res/submarine3.png","res/submarine2.png"]
        super(Player, self).__init__()
        self.pos.x = 40

        self.k_up = False
        self.k_down = False
        self.k_right = False
        self.k_left = False
        self.k_s = False
        self.k_a = False

        self.xfriction = 0.995
        self.yFrame = 20
        self.disableInput = False

            
    def key(self, event):
        if self.disableInput is True: 
            return
        for evt in event:
            if evt.type == KEYDOWN:
                if evt.key == K_UP:
                    self.k_up = True
                if evt.key == K_DOWN:
                    self.k_down = True
                if evt.key == K_a:
                    self.k_a = True
                if evt.key == K_s:
                    self.k_s = True
                if evt.key == K_RIGHT:
                    self.k_right = True
                if evt.key == K_LEFT:
                    self.k_left = True
            elif evt.type == KEYUP:
                if evt.key == K_UP:
                    self.k_up = False
                if evt.key == K_DOWN:
                    self.k_down = False
                if evt.key == K_s:
                    self.k_s = False
                if evt.key == K_a:
                    self.k_a = False
                if evt.key == K_RIGHT:
                    self.k_right = False
                if evt.key == K_LEFT:
                    self.k_left = False
        if self.k_left or self.k_right:
            self.shouldAnimate = True
        else:
            self.shouldAnimate = False

    def event(self, event):
        self.key(event)
        if self.k_right:
            self.acc.x = self.acceleration
        else:
            self.acc.x = -self.friction
            if self.vel.x + self.acc.x < 0:
                self.vel.x = 0
                self.acc.x = 0 
        super(Player, self).event(event)