import pygame

class singleLine:
    def __init__(self, text):
        self.fontObject = pygame.font.Font('freesansbold.ttf', 16)
        self.surfaceObject = self.fontObject.render(text, True, pygame.Color(0,0,0))
        self.rectObject = self.surfaceObject.get_rect()
    def render(self, x, surface):
        self.rectObject.topleft = (10, 10 + 20 * x)
        surface.blit(self.surfaceObject, self.rectObject)

class console:
    def __init__(self):
        self.lineList = []
        self.visible = False
    def out(self, text):
        self.lineList.append(singleLine(text))
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