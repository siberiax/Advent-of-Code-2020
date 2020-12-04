import sys

inp = [int(i) for i in open(sys.argv[1]).readlines()]

for x in range(len(inp)):
    for y in range(len(inp)):
        for z in range(len(inp)):
            if x != y and y != z:
                if inp[x] + inp[y] + inp[z] == 2020:
                    print(inp[x]*inp[y]*inp[z])
                    exit()
