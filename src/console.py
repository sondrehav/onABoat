import pygame

class SingleLine:
    def __init__(self, text):
        self.text = text
        self.fontObject = pygame.font.Font('freesansbold.ttf', 16)
        self.surfaceObject = self.fontObject.render(self.text, True, pygame.Color(0,0,0))
        self.rectObject = self.surfaceObject.get_rect()
    def render(self, x, surface):
        self.rectObject.topleft = (10, 10 + 20 * x)
        surface.blit(self.surfaceObject, self.rectObject)
    def changeText(self, intext):
        self.text = intext

class Console:
    def __init__(self):
        self.lineList = []
        self.visible = True
    def newLine(self, text):
        self.lineList.append(SingleLine(text))
    def render(self, surface):
        if self.visible:
            for i in range(0, len(self.lineList)):
                self.lineList[i].render(i, surface)         
    def show(self):
        self.visible = True
    def hide(self):
        self.visible = False
    def toggle(self):
        if self.visible == False:
            self.visible = True
        else:
            self.visible = False
    def changeLine(self, text, a):
        self.lineList[a].changeText(text)