import re, pygame, math, random
from globals import *

class ParticleFX(object):
    def __init__(self, filename, x, y):
        self.fxFile = filename
        self.f = open(self.fxFile, 'r')
        self.getData(self.f)
        self.f.close()
        self.particles = []
        self.xPos = x
        self.yPos = y
        for i in range(0, self.particleCount):
            self.particles.append(Particle(self.imageName, self.particleSpeedFrom, self.particleSpeedTo, self.particleLifeFrom, self.particleLifeTo, self.particleDirection, self.particleSpread, self.particleXSpread, self.particleYSpread))
        
    def getData(self, file):
        self.table = {}
        regex = re.compile("[\w.,{}()#/]+")
        for line in file.readlines():
            r = re.findall(regex, line)
            if not r:
                continue
            varname = r[0]
            if len(varname) == 0 or varname[0] == "#":
                continue
            value = r[1]
            self.table[varname] = value
        self.imageName = self.table["imageName"]
        self.particleCount = int(self.table["Count"])
        self.particleSpeedFrom = float(self.table["SpeedFrom"])
        self.particleSpeedTo = float(self.table["SpeedTo"])
        self.particleLifeFrom = float(self.table["LifeFrom"])
        self.particleLifeTo = float(self.table["LifeTo"])
        self.particleDirection = int(self.table["Direction"])
        self.particleSpread = int(self.table["Spread"])
        self.particleXSpread = int(self.table["XSpread"])
        self.particleYSpread = int(self.table["YSpread"])
        
    def event(self):
        
        for i in range(0, len(self.particles)):
            self.particles[i].event()
                        
    def render(self, surface):
        for i in range(0, len(self.particles)):
            surface.blit(self.particles[i].getSurf(), (self.xPos + self.particles[i].getX(), self.yPos + self.particles[i].getY()))
            
        
class Particle(object):
    def __init__(self, image, speedFrom, speedTo, lifeFrom, lifeTo, direction, spread, xspread, yspread):
        self.surfaceObject = pygame.image.load(image)
        self.x = 0
        self.y = 0
        self.xspeed = 0
        self.yspeed = 0
        self.i = 0
        self.speedFrom = speedFrom
        self.speedTo = speedTo
        self.lifeFrom = lifeFrom
        self.lifeTo = lifeTo
        self.direction = direction
        self.spread = spread
        self.life = 0
        self.xspread = xspread
        self.yspread = yspread
        self.getRandom()

    def event(self):
        self.i += 1
        if self.i >= (self.life * getFPS()):
            self.i = 0
            self.x = 0
            self.y = 0
            self.getRandom()
        self.x += self.xspeed
        self.y += self.yspeed
        
    def getRandom(self):
        self.randDir = random.uniform(-self.spread, self.spread)
        self.randSpeed = random.uniform(self.speedFrom, self.speedTo)
        self.life = random.uniform(self.lifeFrom, self.lifeTo)
        self.xspeed = math.cos(math.pi * 2 * (self.direction + self.randDir) / 360) * self.randSpeed
        self.yspeed = math.sin(math.pi * 2 * (self.direction + self.randDir) / 360) * self.randSpeed
        self.x = random.randint(0, self.xspread)
        self.y = random.randint(0, self.yspread)

    def getSurf(self):
        return self.surfaceObject
    def getX(self):
        return self.x
    def getY(self):
        return self.y