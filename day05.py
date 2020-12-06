import sys

passes = open(sys.argv[1]).readlines()

ids = []

for p in passes:
    rows = list(range(128))
    cols = list(range(8))

    for c in p:
        if c == 'F':
            rows = rows[:len(rows)//2]
        elif c == 'B':
            rows = rows[len(rows)//2:]
        elif c == 'L':
            cols = cols[:len(cols)//2]
        else:
            cols = cols[len(cols)//2:]

    total = rows[0] * 8 + cols[0]

    ids.append(total)

ids.sort()

for i in range(len(ids)):
    if ids[i] + 2 == ids[i+1]:
        print(ids[i] + 1)
        break
