import sys

data = open(sys.argv[1]).readlines()

nums = [0] * 1000

ticketnums = {}

for i in range(20):
    fields = data[i].split(': ')
    ranges = fields[1].split()
    r1 = ranges[0].split('-')
    r2 = ranges[2].split('-')

    for x in range(int(r1[0]), int(r1[1])):
        nums[x] = 1

    for x in range(int(r2[0]), int(r2[1])):
        nums[x] = 1

    ticketnums[i] = (int(r1[0]), int(r1[1]), int(r2[0]), int(r2[1]))

valid = []

total = 0
for i in range(25,len(data)):
    ns = [int(x) for x in data[i].split(',')]

    good = 1

    for n in ns:
        if nums[n] == 0:
            good = 0
            total += n

    if good:
        valid.append(ns)

print(total)


possibilties = []

for i in range(20):
    possible = list(range(20))
    for ticket in valid:
        num = ticket[i]
        for p in possible:
            rs = ticketnums[p]
            if (num >= rs[0] and num <= rs[1]) or (num >= rs[2] and num <= rs[3]):
                continue
            else:
                possible.remove(p)

    possibilties.append((len(possible), i, possible))

possibilties.sort()

seen = []
map = {}
for p in possibilties:
    for i in p[2]:
        if i not in seen:
            map[i] = p[1]
            seen.append(i)

myticket = [int(i) for i in data[22].split(',')]
total = 1
for i in range(6):
    total *= myticket[map[i]]

print(total)
