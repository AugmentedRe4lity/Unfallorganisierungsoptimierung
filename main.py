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
from time import time
import platform


def main():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

    width, height = 10, 10
    screen = Screen(width, height)

    weights = generate_weights(width, height)
    # draw_grid(screen, color=bg.white)
    # draw_weights(screen, weights)

    while True:
        notarzt = Object(
            randint(0, width - 1) * 4,
            randint(0, height - 1) * 4,
            "N",
            black,
            bg.yellow,
            width=width,
        )
        rettungswagen = Object(
            randint(0, width - 1) * 4,
            randint(0, height - 1) * 4,
            "R",
            black,
            bg.red,
            width=width,
        )
        rw_krankenhaus = Object(
            rettungswagen.x, rettungswagen.y, "+", black, bg.white, width=width
        )
        unfall = Object(
            randint(0, width - 1) * 4,
            randint(0, height - 1) * 4,
            "U",
            black,
            bg.green,
            width=width,
        )

        if (
            notarzt.position != unfall.position
            and unfall.position != rettungswagen.position
            and notarzt.position != rettungswagen.position
        ):
            break
    clear(screen, weights, True)

    if distance(
        shortest_paths_from(rettungswagen.index, weights), unfall.index
    ) < distance(shortest_paths_from(notarzt.index, weights), unfall.index):
        pu = shortest_paths_from(unfall.index, weights)
        pn = shortest_paths_from(notarzt.index, weights)
        w = way(pu, rettungswagen.index)
        dnu = distance(shortest_paths_from(notarzt.index, weights), unfall.index)
        dru = distance(shortest_paths_from(rettungswagen.index, weights), unfall.index)
        l = []
        for i in w:
            iw = pu[i][0]
            id = distance(pn, i)
            dzk = distance(shortest_paths_from(i, weights), rw_krankenhaus.index)
            l.append([dru + iw, id, dzk, i])
        l.reverse()
        ld = {}
        for i in l:
            ld[i[2]] = [i[0], i[1], i[3]]
        mp = -1
        for k, v in ld.items():
            if v[0] >= v[1]:
                mp = v[2]
        if mp == -1:
            screen.show_way(way(pu, rettungswagen.index), bg.white)

            screen.show_object([notarzt, rettungswagen, unfall])
            screen.display()
            # return 1
        else:
            screen.show_way(way(pu, rettungswagen.index), bg.white)
            screen.show_way(way(pn, mp), bg.red)

            screen.show_object([notarzt, rettungswagen, unfall])
            screen.display()
            # return 2

    else:
        screen.show_way(
            way(shortest_paths_from(unfall.index, weights), rettungswagen.index),
            bg.white,
        )
        screen.show_way(
            way(shortest_paths_from(unfall.index, weights), notarzt.index), bg.red
        )

        screen.show_object([notarzt, rettungswagen, unfall])
        screen.display()
        # return 3


if "__main__" == __name__:
    main()
