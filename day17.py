import sys
from collections import defaultdict
from copy import copy

data = open(sys.argv[1]).readlines()

space = []

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '#':
            space.append((0,x,y,0))

for _ in range(6):
    neighbors = defaultdict(int)
    for node in space:
        for x in range(-1,2):
            for y in range(-1,2):
                for z in range(-1,2):
                    for a in range(-1,2):
                        if x or y or z or a:
                            neighbors[(node[0] + x, node[1] + y, node[2] + z, node[3] + a)] += 1

    newspace = []
    for n in neighbors:
        if n in space:
            if neighbors[n] == 3 or neighbors[n] == 2:
                newspace.append(n)
        else:
            if neighbors[n] == 3:
                newspace.append(n)

    space = copy(newspace)

print(len(space))
