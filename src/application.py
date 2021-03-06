import pygame, sys
from pygame.locals import *
from entity import *
from player import *
from bubble import *
from console import Console
from globals import *
from background import *


class Application:
    entitylist = [[],[],[]] # 2D array - [0] er bak, [1] er player, [2] er forran

    def __init__(self):
        self.width = getWidth()
        self.height = getHeight()

        self.fps = getFPS()
        self.bubbleCount = int(getWidth() / 160)
        self.drawBubbles = True
        self.drawBG = True
        
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        if fullscreen():
            self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Anim')
        
        pygame.mouse.set_visible(cursor())
        
        for i in range(0, self.bubbleCount):
            self.entitylist[2].append(Bubble(True))
            self.entitylist[0].append(Bubble(False))
        
        self.player = Player()
        self.entitylist[1].append(self.player)
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

        for lst in self.entitylist:
            for e in lst:
                if isinstance(e, Bubble):
                    e.setXSpeedFromPlayer(-self.player.getXSpeed())
                e.event(self.events)
            
    def render(self):
        #Background
        if self.drawBG: self.background.render(self.windowSurfaceObj)
        for lst in self.entitylist:
            for e in lst:
                e.render(self.windowSurfaceObj, self.DrawPosVector)
        #Konsollen
        self.console.render(self.windowSurfaceObj)
        pygame.display.update()
        self.fpsClock.tick(getFPS())
        

    def exit(self):
        pygame.event.post(pygame.event.Event(QUIT))

    def fullscreen(self, input):
        if input:
            self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        else:
            self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height))
