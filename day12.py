import sys
from copy import copy

data = open(sys.argv[1]).readlines()

curr = [0,0]
wp = [10,1]

dirs = [(1,1), (-1,1), (-1,-1), (1,-1)]

for d in data:
    l = d[0]
    n = int(d[1:])

    if l == 'F':
        orig = copy(wp)
        for i in range(n):
            curr[0] += wp[0]
            curr[1] += wp[1]
    elif l == 'E':
        wp[0] += n
    elif l == 'W':
        wp[0] -= n
    elif l == 'N':
        wp[1] += n
    elif l == 'S':
        wp[1] -= n
    elif l == 'L':
        m = 0
        for i in range(n // 90):
            wp[0], wp[1] = wp[1], wp[0]
            m += 1
        wp[0] *= dirs[m][0]
        wp[1] *= dirs[m][1]
    else:
        m = 0
        for i in range(n // 90):
            wp[0], wp[1] = wp[1], wp[0]
            m -= 1
        wp[0] *= dirs[m][0]
        wp[1] *= dirs[m][1]

print(abs(curr[0]) + abs(curr[1]))
