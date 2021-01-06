from pprint import pprint
from ansi.colour.fg import *
from ansi.colour import bg
from random import randint

from functions import *
from variables import log_blend_colours
from screen import Screen
from object import Object

if '__main__' == __name__:
    width, height = 20, 10
    screen = Screen(width, height)

    weights = generate_weights(width, height)
    print(screen.size())
    draw_grid(screen, color=bg.white)
    draw_weights(screen, weights)

    # while True:
    #     notarzt = Object(randint(0,3)*4, randint(0,3)*4, 'N', yellow, bg.red, width=width)
    #     krankenhaus = Object(randint(0,3)*4, randint(0,3)*4, '+', red, bg.white, width=width)
    #     krankenwagen = Object(randint(0,3)*4, randint(0,3)*4, 'W', red, bg.yellow, width=width)
    #     if notarzt.position != krankenhaus.position and krankenhaus.position != krankenwagen.position:
    #         break

    # screen.show_object([notarzt, krankenhaus, krankenwagen])

    screen.display()
