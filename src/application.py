import pygame, sys
from pygame.locals import *
from entity import *
from player import *
from bubble import *

class Application:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.fps = 60
        
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Anim')
        
        self.entityList = []
        self.bubbleList = []
        
        self.player = Player()
        self.bubble = Bubble()
        print('Init...')
    def event(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    print('Exiting...')
                    self.exit()
        self.player.event(self.events)
    def render(self):
        self.windowSurfaceObj.fill(pygame.Color(50,60,121))
        self.bubble.render(self.windowSurfaceObj)
        self.player.render(self.windowSurfaceObj)
        pygame.display.update()
        self.fpsClock.tick(self.fps)
    def exit(self):
        pygame.event.post(pygame.event.Event(QUIT))