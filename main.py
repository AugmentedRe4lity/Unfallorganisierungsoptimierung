from pprint import pprint
from ansi.colour.fg import *
from ansi.colour import bg
from random import randint
import sys
from os import system
from time import sleep

from functions import *
from variables import log_blend_colours
from screen import Screen
from object import Object

if '__main__' == __name__:
    system('cls')
    width, height = 10,10
    screen = Screen(width, height)

    weights = generate_weights(width, height)
    # draw_grid(screen, color=bg.white)
    # draw_weights(screen, weights)

    while True:
        notarzt = Object(randint(0,width-1)*4, randint(0,height-1)*4, 'N', black, bg.yellow, width=width)
        krankenhaus = Object(randint(0,width-1)*4, randint(0,height-1)*4, '+', black, bg.white, width=width)
        krankenwagen = Object(randint(0,width-1)*4, randint(0,height-1)*4, 'R', black, bg.red, width=width)
        unfall = Object(randint(0,width-1)*4, randint(0,height-1)*4, 'U', black, bg.green, width=width)

        if notarzt.position != krankenhaus.position and krankenhaus.position != krankenwagen.position:
            break

    path={}
    path['KU'] = [shortest_paths_from(krankenwagen.index, weights), unfall.index, 1, 0, bg.red, krankenwagen]
    path['NU'] = [shortest_paths_from(notarzt.index, weights), unfall.index, 1, 0, bg.blue, notarzt]
    path['UK'] = [shortest_paths_from(unfall.index, weights), krankenhaus.index, 1, 0, bg.white, unfall]

    while any([path[i][2]<len(way(path[i])) for i in path.keys()]):
        clear(screen, weights, True if len(sys.argv)==2 else False)
        for i in path.keys():
            path[i][3] += 1
            if path[i][2]<len(way(path[i])):
                print(i)
                if path[i][3] == path[i][0][way(path[i])[path[i][2]]][0]:
                    path[i][2]+=1
            # screen.show_way(way(path[i]), path[i][4],bis=path[i][2])
            path[i][5].set_i(way(path[i])[path[i][2]-1])
        screen.show_object([path['KU'][5], path['NU'][5], path['UK'][5], krankenhaus])
        screen.display()
        sleep(0.1)
