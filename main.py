from pprint import pprint
from ansi.colour.fg import *
from ansi.colour import bg
from random import randint
import sys
from os import system

from functions import *
from variables import log_blend_colours
from screen import Screen
from object import Object

if '__main__' == __name__:
    system('cls')
    width, height = 20, 10
    screen = Screen(width, height)

    weights = generate_weights(width, height)
    print(screen.size())
    draw_grid(screen, color=bg.white)
    draw_weights(screen, weights)

    while True:
        notarzt = Object(randint(0,width-1)*4, randint(0,height-1)*4, 'N', yellow, bg.white, width=width)
        krankenhaus = Object(randint(0,width-1)*4, randint(0,height-1)*4, '+', red, bg.white, width=width)
        krankenwagen = Object(randint(0,width-1)*4, randint(0,height-1)*4, 'W', red, bg.white, width=width)
        if notarzt.position != krankenhaus.position and krankenhaus.position != krankenwagen.position:
            break

    screen.show_object([notarzt, krankenhaus, krankenwagen])

    screen.display(debug=True if len(sys.argv)==2 else False)
