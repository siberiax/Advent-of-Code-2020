import sys

data = [int(i) for i in open(sys.argv[1])]

key = 0

for i in range(25,len(data)):
    found = False
    for x in range(i-25,i):
        for y in range(i-25,i):
            if data[x] != data[y] and data[x] + data[y] == data[i]:
                found = True
                break
        if found:
            break

    if not found:
        key = data[i]
        break

for x in range(len(data)):
    found = False
    for y in range(x,len(data)):
        if x != y and sum(data[x:y]) == key:
            print(min(data[x:y]) + max(data[x:y]))
            found = True
            break
        elif sum(data[x:y]) > key:
            break

    if found:
        break
