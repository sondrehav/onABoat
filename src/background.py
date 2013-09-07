import pygame
from entity import Entity
from globals import *

class Background(Entity):
    def __init__(self):
        self.imageNames = ["res/background.png"]
        super(Background, self).__init__()
        self.surfaceObjects[0] = pygame.transform.scale(self.surfaceObjects[0], (int((self.width/self.height)*getHeight()), int(getHeight())))
        self.yPos = 0
        self.xPos = 0
    def event(self, event):
        super(Background, self).event(event)
