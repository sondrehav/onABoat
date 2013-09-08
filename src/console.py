import pygame

class SingleLine:
    textcolor = pygame.Color(220,220,220)
    textSize = 12
    textFont = "courier"

    def __init__(self, text):
        self.text = text
        self.fontObject = pygame.font.Font('freesansbold.ttf', self.textSize)
        self.surfaceObject = self.fontObject.render(self.text, True, self.textcolor)
        self.rectObject = self.surfaceObject.get_rect()

    def render(self, x, y, surface):
        self.rectObject.topleft =(x,y) 
        surface.blit(self.surfaceObject, self.rectObject)

    def changeText(self, intext):
        self.text = intext

class Console:

    def __init__(self, width, height):
        self.lineList = []
        self.visible = False
        self.xPos = 10
        self.yPos = 10
        self.lineSpacing = SingleLine.textSize + 4
        self.currentLine = ""
        self.bsurface = pygame.Surface((width, height))
        self.bsurface.set_alpha(128)
        self.bsurface.fill((0,0,0))

    def out(self, text):
        self.lineList.append(SingleLine(text))
        self.currentLine = text

    def render(self, surface):
        if self.visible:
            surface.blit(self.bsurface,(0,0))
            for i in range(0, len(self.lineList)):
                index = len(self.lineList) - i - 1
                self.lineList[index].render(self.xPos, self.yPos + (i * self.lineSpacing), surface)            

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

