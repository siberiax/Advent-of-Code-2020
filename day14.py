import sys

data = [l.strip() for l in open(sys.argv[1])]

mem = {}
mask = ""

for d in data:
    if "mask" in d:
        fields = d.split(' = ')
        mask = fields[1]
    else:
        fields = d.split(' = ')
        bin = "{0:b}".format(int(fields[1]))
        bin = "0" * (len(mask) - len(bin)) + bin
        new = ""
        for i in range(len(bin)):
            if mask[i] == "X":
                new += bin[i]
            else:
                new += mask[i]

        mem[fields[0].split('[')[1][:-1]] = int(new, 2)

total = 0
for m in mem:
    total += mem[m]

print(total)

mem = {}
mask = ""

for d in data:
    if "mask" in d:
        fields = d.split(' = ')
        mask = fields[1]
    else:
        fields = d.split(' = ')

        memaddr = int(fields[0].split('[')[1][:-1])

        memaddrs = []

        top = 2 ** mask.count('X')
        toplen = len("{0:b}".format(top-1))
        for i in range(top):
            bin = "{0:b}".format(i)
            bin = "0" * (toplen - len(bin)) + bin
            binstr = "{0:b}".format(memaddr)
            binstr = "0" * (len(mask) - len(binstr)) + binstr

            new = ""
            xcount = 0
            for i in range(len(mask)):
                if mask[i] == '0':
                    new += binstr[i]
                elif mask[i] == '1':
                    new += "1"
                else:
                    new += bin[xcount]
                    xcount += 1

            memaddrs.append(new)

        for addr in memaddrs:
            mem[addr] = int(fields[1])

total = 0
for m in mem:
    total += mem[m]

print(total)
