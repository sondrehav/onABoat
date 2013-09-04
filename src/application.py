import pygame, sys
from pygame.locals import *
from entity import *
from player import *
from bubble import *
from console import Console


class Application:
    def __init__(self):
        self.width = 1024
        self.height = 768
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
        self.console = Console()
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
                        s = self.console.getCurrentLine()
                        try:
                            exec(s)
                        except:
                            print(s)
                            print(sys.exc_info()[0])
                        self.console.stageCurrentLine()
                        break
                    elif event.key == K_BACKSPACE:
                        self.console.setCurrentLine(self.console.getCurrentLine()[:-1])
                        break
                    self.console.appendCurrentLine(event.unicode)
            
        self.player.event(self.events)

    def render(self):
        self.windowSurfaceObj.fill(pygame.Color(50,60,121))
        self.bubble.render(self.windowSurfaceObj, self.DrawPosVector)
        self.player.render(self.windowSurfaceObj, self.DrawPosVector)
        self.console.render(self.windowSurfaceObj)
        pygame.display.update()
        self.fpsClock.tick(self.fps)
        

    def exit(self):
        pygame.event.post(pygame.event.Event(QUIT))

