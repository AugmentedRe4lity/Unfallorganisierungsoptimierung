from pprint import pprint
from ansi.colour.fg import *
from ansi.colour import bg
from random import randint

from functions import *
from variables import log_blend_colours
from screen import Screen
from object import Object

if '__main__' == __name__:
    width, height = 4, 4
    screen = Screen(width, height)

    weights = generate_weights(width, height)
    print(screen.size())
    draw_grid(screen, color=bg.white)
    draw_weights(screen, weights)


    screen.display()

    shortest_paths_from(0, weights)
