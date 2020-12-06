import sys
from collections import defaultdict

data = open(sys.argv[1]).readlines()

groups  = []

curr = []
for d in data:
    if d == '\n':
        groups.append(curr)
        curr = []
    else:
        curr.append(d.strip())

groups.append(curr)

total = 0

for g in groups:
    seen = defaultdict(int)
    for p in g:
        for c in p:
            seen[c] += 1

    for l in seen:
        if seen[l] == len(g):
            total += 1

print(total)
