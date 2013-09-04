import pygame

class SingleLine:

    def __init__(self, text):
        self.fontObject = pygame.font.Font('freesansbold.ttf', 16)
        self.surfaceObject = self.fontObject.render(text, True, pygame.Color(0,0,0))
        self.rectObject = self.surfaceObject.get_rect()

    def render(self, x, y, surface):
        self.rectObject.topleft =(x,y) 
        surface.blit(self.surfaceObject, self.rectObject)

class Console:

    def __init__(self):
        self.lineList = []
        self.visible = False
        self.xPos = 10
        self.yPos = 10
        self.currentLine = ""

    def out(self, text):
        self.lineList.append(SingleLine(text))
        self.currentLine = text

    def render(self, surface):
        if self.visible:
            for i in range(0, len(self.lineList)):
                index = len(self.lineList) - i - 1
                self.lineList[index].render(self.xPos, self.yPos + (i * 20), surface)            

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def toggle(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False

    def isActive(self):
        return self.visible

    def getCurrentLine(self):
        return self.currentLine

    def setCurrentLine(self, text):
        self.currentLine = text
        if(len(self.lineList) == 0):
            self.out(self.currentLine)
        else:
            self.lineList[-1] = SingleLine(text)

    def appendCurrentLine(self, text):
        self.setCurrentLine(self.getCurrentLine() + text)
    
    def stageCurrentLine(self):
        self.out("")

