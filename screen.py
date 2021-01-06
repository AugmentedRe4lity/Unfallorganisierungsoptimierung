from ansi.colour.fg import *
from ansi.colour import bg
from os import system

class Screen:
    def __init__(self, width, height, foreground=None, background=None):
        self.screen = [[" " for _ in range(width*3+1)] for _ in range(height*3+1)]
        self.width = width
        self.height = height
        self.background = background if background!=None else bg.black
        self.foreground = foreground if foreground!=None else white

    def set(self, x, y, c, background=None, foreground=None):
        background = str(background) if background!=None else str(self.background)
        foreground = str(foreground) if foreground!=None else str(self.foreground)
        print(x, y)
        self.screen[y][x] = background+foreground+c+str(self.background)+str(self.foreground)

    def show_object(self, objects):
        for object in objects:
            self.set(object.x, object.y, object.label, object.bg, object.fg)

    def display(self):
        #system('clear')
        print('\n'.join([' '.join([j for j in i]) for i in self.screen]))

    def size(self):
        return (self.width, self.height)
