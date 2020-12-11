import sys
from copy import deepcopy

def occupied():
    occupied = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == '#':
                occupied += 1
    return occupied

grid = [list(x.strip()) for x in open(sys.argv[1])]

part2 = deepcopy(grid)

w = len(grid[0])
h = len(grid)

while True:
    prev = deepcopy(grid)

    for y in range(h):
        for x in range(w):
            cd = [
                (y-1, x-1),
                (y-1, x),
                (y-1, x+1),
                (y, x-1),
                (y, x+1),
                (y+1, x-1),
                (y+1, x),
                (y+1, x+1)
                ]

            neighbors = []
            if x == 0 and y == 0:
                neighbors = [cd[4], cd[6], cd[7]]
            elif x == w-1 and y == 0:
                neighbors = [cd[3], cd[5], cd[6]]
            elif x == 0 and y == h-1:
                neighbors = [cd[1], cd[2], cd[4]]
            elif x == w-1 and y == h-1:
                neighbors = [cd[0], cd[1], cd[3]]
            elif x == 0:
                neighbors = [cd[1], cd[2], cd[4], cd[6], cd[7]]
            elif x == w-1:
                neighbors = [cd[0], cd[1], cd[3], cd[5], cd[6]]
            elif y == 0:
                neighbors = [cd[3], cd[4], cd[5], cd[6], cd[7]]
            elif y == h-1:
                neighbors = [cd[0], cd[1], cd[2], cd[3], cd[4]]
            else:
                neighbors = cd

            total = 0
            for n in neighbors:
                if prev[n[0]][n[1]] == '#':
                    total += 1

            if prev[y][x] == 'L' and total == 0:
                grid[y][x] = '#'
            elif prev[y][x] == '#' and total >= 4:
                grid[y][x] = 'L'
    if grid == prev:
        break

print(occupied())

grid = deepcopy(part2)

while(True):
    prev = deepcopy(grid)

    for y in range(h):
        for x in range(w):

            if prev[y][x] == '.':
                continue

            dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

            total = 0

            for d in dirs:
                ny = y
                nx = x
                found = False
                ny += d[0]
                nx += d[1]
                while ny >= 0 and nx >= 0 and ny <= h-1 and nx <= w-1:
                    if prev[ny][nx] != '.':
                        found = True
                        break
                    ny += d[0]
                    nx += d[1]
                if found:
                    if prev[ny][nx] == '#':
                        total += 1

            if prev[y][x] == 'L' and total == 0:
                grid[y][x] = '#'
            elif prev[y][x] == '#' and total >= 5:
                grid[y][x] = 'L'

    if grid == prev:
        break

print(occupied())
