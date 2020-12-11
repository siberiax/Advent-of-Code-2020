import sys
from functools import lru_cache

data = [int(i) for i in open(sys.argv[1])]

data.sort()

data.append(data[-1] + 3)

curr = 0
onecount = 0
threecount = 0

for i in data:
    if i == curr+1:
        onecount += 1
    elif i == curr+3:
        threecount += 1
    curr = i

print(onecount * threecount)

@lru_cache(maxsize = 1000)
def paths(num):
    if num == data[-1]:
        return 1
    else:
        next = []
        for i in range(1,4):
            if num + i in data:
                next.append(num + i)
        return sum(map(lambda x: paths(x), next))

print(paths(0))
