import sys

data = [line.strip() for line in open(sys.argv[1])]

bg = dict()

for bag in data:
    fields = bag.split(' bags contain ')
    bigger = fields[0]

    all_inside = fields[1].replace('.', ',').split(',')[:-1]

    inside = []
    for b in all_inside:
        inside.append(' '.join(b.split()[:-1]))

    bg[bigger] = inside

total = 0

for bag in bg:
    queue = [bag]
    while len(queue):
        curr = queue.pop(0)

        if curr == "shiny gold" and bag != curr:
            total += 1
            break

        inside = bg[curr]
        for b in inside:
            name = ' '.join(b.split()[1:])
            if name != 'other':
                queue.append(name)

print(total)

total2 = 0

queue = [(1,"shiny gold")]
while len(queue):
    curr = queue.pop(0)
    mult = curr[0]
    total2 += mult
    inside = bg[curr[1]]
    for b in inside:
        parts = b.split()
        if len(parts) > 2:
            amt = int(parts[0])
            name = ' '.join(parts[1:])
            queue.append((amt*mult, name))


print(total2 - 1)
