from ansi.colour.fg import *
from ansi.colour import bg
from os import system
import platform


class Screen:
    def __init__(self, width, height, foreground=None, background=None):
        self.screen = [
            [" " for _ in range(width * 3 + (width - 3))] for _ in range(height * 3 + (height - 3))
        ]
        self.width = width
        self.height = height
        self.background = background if background != None else bg.black
        self.foreground = foreground if foreground != None else white

    def clear(self, debug=False):
        os_platform = platform.system()
        if not debug:
            if os_platform == "Windows":
                system("cls")
            else:
                system("clear")
        self.screen = [
            [" " for _ in range(self.width * 3 + (self.width - 3))]
            for _ in range(self.height * 3 + (self.height - 3))
        ]

    def set(self, x, y, c, background=None, foreground=None):
        background = str(background) if background != None else str(self.background)
        foreground = str(foreground) if foreground != None else str(self.foreground)
        if (
            x >= 0
            and x < 3 * self.width + (self.width - 3)
            and y >= 0
            and y < 3 * self.height + (self.height - 3)
        ):
            self.screen[y][x] = (
                background
                + foreground
                + c
                + str(self.background)
                + str(self.foreground)
            )

    def show_object(self, objects):
        for object in objects:
            self.set(object.x, object.y, object.label, object.bg, object.fg)
            self.set(object.x - 1, object.y - 1, "\\")
            self.set(object.x - 1, object.y + 1, "/")
            self.set(object.x + 1, object.y + 1, "\\")
            self.set(object.x + 1, object.y - 1, "/")

    def show_way(self, way, background, von=0, bis=None):
        px, py = way[von] % self.width * 4, way[von] // self.width * 4

        for i in way[von:bis]:
            x, y = i % self.width * 4, i // self.width * 4

            self.set(x, y, " ", background)
            for nx in range(px, x):
                if nx % 4 != 2:
                    self.set(nx, y, " ", background)
            for ny in range(py, y):
                if ny % 4 != 2:
                    self.set(x, ny, " ", background)
            for nx in range(px, x, -1):
                if nx % 4 != 2:
                    self.set(nx, y, " ", background)
            for ny in range(py, y, -1):
                if ny % 4 != 2:
                    self.set(x, ny, " ", background)

            px, py = x, y

    def display(self):
        print("\n".join([" ".join([j for j in i]) for i in self.screen]))

    def size(self):
        return (self.width, self.height)
