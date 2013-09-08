import math, pygame

class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getLength(self):
        return math.sqrt(self.x**2 + self.y**2)

    def setLength(self, val):
        l = getLength()
        self.x *= val/l
        self.y *= val/l

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __mul__(self, v):
        return Vector(self.x * v.x, self.y * v.y)

    def __str__(self):
        return "[{0}, {1}]".format(self.x, self.y)
