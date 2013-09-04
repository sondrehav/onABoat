import pygame

class msgBox:
    def __init__(self, text, x, y):
        self.fontObject = pygame.font.Font('freesansbold.ttf', 24)
        self.surfaceObject = self.fontObject.render(text, True, pygame.Color(70,70,70))
        self.rectObject = self.surfaceObject.get_rect()
        self.rectObject.topleft = (x,y)
    def render(self, surface):
        surface.blit(self.surfaceObject, self.rectObject)