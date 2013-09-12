import pygame, sys
from pygame.locals import *
from entity import *
from player import *
from bubble import *
from camera import Camera
from console import Console
from globals import *
from background import *
from particleFX import ParticleFX

class Application:
    entitylist = [[],[],[]] # 3D array - [0] er bak, [1] er player, [2] er forran

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
        
        self.camera = Camera()

        self.particle01 = ParticleFX('particleFXtest01.txt',getWidth(),0)

        self.camera.entitylock = self.player
        
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
            
        self.background.event(self.events)
        self.particle01.event()

        for lst in self.entitylist:
            for e in lst:
                e.event(self.events)
                if e.safeToDelete:
                    if e.pos.x < self.camera.x-self.camera.width:
                        lst.remove(e)
        self.camera.update()
        
            
    def render(self):
        #Background
        if self.drawBG: self.background.render(self.windowSurfaceObj, -self.camera.x, -self.camera.y)
        for lst in self.entitylist:
            for e in lst:
                x = e.pos.x - self.camera.x
                y = e.pos.y - self.camera.y
                e.render(self.windowSurfaceObj,x, y, self.DrawPosVector)
                
        self.particle01.render(self.windowSurfaceObj)        
        
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

