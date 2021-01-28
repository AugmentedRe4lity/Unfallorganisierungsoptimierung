from random import randint
from numpy import mean
from ansi.colour.fg import *
from ansi.colour import bg
from variables import *
from pprint import pprint

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
            weights[i].append([i+width, w, log_blend_colours[len(log_blend_colours)-w-2]])
        if i%width+1<width:
            w = randint(1,9)
            weights[i].append([i+1, w, log_blend_colours[len(log_blend_colours)-w-2]])

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

def sort_dict(d):
    keys = [key for key in d.keys()]
    keys.sort()
    rd = {}
    for key in keys:
        rd[key]=d[key]
    return rd

def shortest_paths_from(index, weights):
    visited = []
    unvisited = [i for i in range(len(weights))]
    s_paths = {index: [0, index]}
    o = {}
    c_index = index
    c_weight = weights[index]

    while True:
        for i in c_weight:
            if i[0] in unvisited:
                un = i[0]
                w = i[1]

                if un in s_paths.keys():
                    dist = s_paths[un][0]
                    if dist>s_paths[c_index][0]+w:
                        s_paths[un][0] = s_paths[c_index][0]+w
                        s_paths[un][1] = c_index
                else:
                    s_paths[un] = [s_paths[c_index][0]+w, c_index]
        visited.append(c_index)
        unvisited.remove(c_index)

        sd = -1
        sk = -1

        for key, value in s_paths.items():
            if key in unvisited:
                if sd==-1:
                    sd = value[0]
                    sk = key
                elif value[0]<sd:
                    sd = value[0]
                    sk = key
        c_index = sk
        c_weight = weights[c_index]

        if len(unvisited)==0:
            #print(sort_dict(s_paths), '\ndone')
            break

    return sort_dict(s_paths)

def distance(path, target=None):
    if target == None:
        target = path[1]
        path = path[0]
    return path[target][0]

def way(path, target=None):
    if target == None:
        target = path[1]
        path = path[0]
    way = [target]
    start = -1
    for key, value in path.items():
        if key == value[1]:
            start = key
    i = target
    while i!=start:
        way.append(path[i][1])
        i = path[i][1]
    way.reverse()
    return way

def fast_meet(p1, p2):
    min = -1
    j = 0
    for i in range(len(p1)):
        if min==-1 or p1[i][0]+p2[i][0]<min:
            min = p1[i][0]+p2[i][0]
            j = i
    return j, min

def clear(screen, weights, debug):
    screen.clear(debug=debug)
    draw_grid(screen, color=bg.white)
    draw_weights(screen, weights)
