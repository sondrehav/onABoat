import pygame, sys
from pygame.locals import *
from entity import *
from player import *
from bubble import *
from console import Console
from globals import *
from background import *


class Application:
    def __init__(self):
        self.width = getWidth()
        self.height = getHeight()
        self.bubbleCount = int(getWidth() / 40)
        
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        if fullscreen():
            self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Anim')
        
        pygame.mouse.set_visible(cursor())
        
        self.entityList = []
        self.bubbleListFront = []
        self.bubbleListBack = []
                
        for i in range(0, self.bubbleCount):
            self.bubbleListFront.append(Bubble(True))
            self.bubbleListBack.append(Bubble(False))
        
        self.player = Player()
        self.background = Background()
        
        print('Init...')
        self.console = Console(getWidth(), getHeight())
        Console.host = self
        self.DrawPosVector = False

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
            if event.type == KEYDOWN:
                if event.key == K_F12:
                    self.console.toggle()

                elif self.console.isActive():
                    if event.key == K_RETURN:
                        self.console.execute()
                        break
                    elif event.key == K_BACKSPACE:
                        self.console.setCurrentLine(self.console.getCurrentLine()[:-1])
                        break
                    self.console.appendCurrentLine(event.unicode)
                    return
            
        self.background.dirVector.setX(-(self.player.getXSpeed() / 8))
        self.background.event(self.events)

        self.player.event(self.events)
        for i in range(0, self.bubbleCount):
            self.bubbleListFront[i].event(self.events)
            self.bubbleListFront[i].setXSpeedFromPlayer(-self.player.getXSpeed())
            self.bubbleListBack[i].event(self.events)
            self.bubbleListBack[i].setXSpeedFromPlayer(-self.player.getXSpeed())
            
    def render(self):
        #Background
        self.background.render(self.windowSurfaceObj)
        #Boblene bak
        for i in range(0, self.bubbleCount):
            self.bubbleListBack[i].render(self.windowSurfaceObj, self.DrawPosVector)
        #Spilleren
        self.player.render(self.windowSurfaceObj, self.DrawPosVector)
        #Boblene forran
        for i in range(0, self.bubbleCount):
            self.bubbleListFront[i].render(self.windowSurfaceObj, self.DrawPosVector)
        
        #Konsollen
        self.console.render(self.windowSurfaceObj)
        pygame.display.update()
        self.fpsClock.tick(getFPS())
        

    def exit(self):
        pygame.event.post(pygame.event.Event(QUIT))

