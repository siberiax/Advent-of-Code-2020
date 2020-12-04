import sys

data = open(sys.argv[1]).readlines()

total = 0
total2 = 0

for line in data:
    fields = line.split()
    r = fields[0].split('-')
    low = int(r[0])
    high = int(r[1])

    letter = fields[1][0]

    count = 0
    for c in fields[2]:
        if c == letter:
            count += 1

    if count >= low and count <= high:
        total += 1

    c1 = fields[2][low-1]
    c2 = fields[2][high-1]

    if [c1,c2].count(letter) == 1:
        total2 += 1

print(total)
print(total2)
