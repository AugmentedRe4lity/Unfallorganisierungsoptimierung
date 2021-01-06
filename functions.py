from random import randint
from numpy import mean
from ansi.colour.fg import *
from ansi.colour import bg
from variables import *

def draw_grid(screen, color=''):
    color = color if color!=None else bg.black
    width, height = screen.size()
    for y in range(height):
        for i in range(3*width+(width-4)): screen.set(i, y*4, '-')
    for x in range(width):
        for i in range(3*height+(height-4)): screen.set(x*4, i, '|')
        for y in range(height):
            screen.set(x*4, y*4, 'x')


def generate_weights(width, height):
    weights = [[] for _ in range(width*height)]

    for i in range(width*height):
        if i+width<width*height:
            w = randint(1,9)
            weights[i].append([i+width, w, log_blend_colours[w-1]])
        if i%width+1<width:
            w = randint(1,9)
            weights[i].append([i+1, w, log_blend_colours[w-1]])

    for i, point in enumerate(weights):
        for weight in point:
            index = weight[0]
            ws = weight[1]
            w = weight[2]

            if not any([ind == i for ind in [wts[0] for wts in weights[index]]]): weights[index].append([i,ws,w])


    return weights

def draw_weights(screen, weights):
    width = screen.width
    for i, item in enumerate(weights):
        x = i%width * 4
        y = i//width * 4

        for weight in item:
            char = str(weight[1])
            color = weight[2]

            index = weight[0]
            nx, ny = index%width * 4, index//width * 4

            screen.set(int(mean([x, nx])), int(mean([y, ny])), char, foreground=color)
