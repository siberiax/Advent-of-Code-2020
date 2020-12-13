import sys

data = open(sys.argv[1]).readlines()

tstamp = int(data[0])
buses = data[1].strip().split(',')

wait = 9999999999
busid = 0
for b in buses:
    if b != 'x':
        n = int(b)
        w = n - (tstamp % n)

        if w < wait:
            wait = w
            busid = n

print(busid * wait)

bd = {}

for i in range(len(buses)):
    if buses[i] != 'x':
        bd[int(buses[i])] = i


s = 1
a = 1
for num in bd:
    print(num)
    if bd[num] == 0:
        s = num
        a = num
    else:
        while num - (s % num) != bd[num] % num:
            s += a
        a *= num

print(s)
