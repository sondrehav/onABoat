import pygame, sys
from pygame.locals import *
from application import *

app = Application()

while True:    
    app.event()
    app.render()