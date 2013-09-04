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
        self.bubbleCount = 10
        
        pygame.init()
        self.fpsClock = pygame.time.Clock()
        self.windowSurfaceObj = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Anim')
        
        self.entityList = []
        self.bubbleListFront = []
        self.bubbleListBack = []
                
        for i in range(0, self.bubbleCount):
            self.bubbleListFront.append(Bubble(True))
            self.bubbleListBack.append(Bubble(False))
        
        self.player = Player()
        #self.backGround
        
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
        for i in range(0, self.bubbleCount):
            self.bubbleListFront[i].event(self.events)
            self.bubbleListBack[i].event(self.events)

    def render(self):
        self.windowSurfaceObj.fill(pygame.Color(50,60,121))
        for i in range(0, self.bubbleCount):
            self.bubbleListBack[i].render(self.windowSurfaceObj)
        self.player.render(self.windowSurfaceObj, self.DrawPosVector)
        for i in range(0, self.bubbleCount):
            self.bubbleListFront[i].render(self.windowSurfaceObj, self.DrawPosVector)

        pygame.display.update()
        self.fpsClock.tick(self.fps)
        

    def exit(self):
        pygame.event.post(pygame.event.Event(QUIT))

