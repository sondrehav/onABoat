import math, pygame

class Vector:
    def __init__(self, length, direction):
        self.x = math.cos(direction) * length
        self.y = math.sin(direction) * length
        self.length = math.fabs(length)
        self.direction = direction
        self.xPos = 0
        self.yPos = 0

    def setDirection(self, d):
        self.direction = d
        self.x = math.cos(self.direction) * self.length
        self.y = math.sin(self.direction) * self.length

    def getDirection(self):
        return self.direction

    def setLength(self, l):
        self.length = math.fabs(l)
        self.x = math.cos(self.direction) * self.length
        self.y = math.sin(self.direction) * self.length

    def getLength(self):
        return self.length

    def setX(self, x):
        self.x = x
        self.direction = math.atan2(self.y, self.x)
        self.length = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y
        self.direction = math.atan2(self.y, self.x)
        self.length = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def getY(self):
        return self.y

    def printVector(self):
        print('X: ',self.x, ', Y: ',self.y,', Direction: ',self.direction,', Length: ',self.length)

    def render(self, surface):
        self.sourceSurface = pygame.Surface((surface.get_width(),surface.get_height()))

        color = pygame.Color(255,0,0)   
        startpos = (self.xPos, self.yPos)
        endpos = ((self.getX() * 16 + startpos[0]), (self.getY() * 16 + startpos[1]))

        pygame.draw.line(self.sourceSurface, color, startpos, endpos, 3)
        surface.blit(self.sourceSurface, (0 , 0), None, pygame.BLEND_ADD)
