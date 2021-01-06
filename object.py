from ansi.colour.fg import *
from ansi.colour import bg
from time import sleep

class Object:

    def __init__(self, x, y, label, foregroundcolor=white, backgroundcolor=bg.black, width=4):
        self.x, self.y = x, y
        self.position = (x, y)
        self.label = label
        self.fg = foregroundcolor
        self.bg = backgroundcolor
        self.index = int(x/4+y*width/4)

    def move(self, x, y):
        sleep(1)
        self.x += x
        self.y += y
