import sys

expected = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

hex = "abcdef0123456789"
hcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
nums = "0123456789"

expected.sort()

data = open(sys.argv[1]).readlines()

entries = []

curr = ""

for line in data:
    if line == '\n':
        entries.append(curr)
        curr = ""
    else:
        curr += line

entries.append(curr)

good = []

for entry in entries:
    pieces = []
    fields = entry.split()
    for f in fields:
        pieces.append(f[:3])

    if 'cid' not in pieces:
        pieces.append('cid')

    pieces.sort()

    if pieces == expected:
        good.append(fields)

total = 0

for entry in good:
    bad = 0
    for field in entry:

        kv = field.split(':')
        k = kv[0]
        v = kv[1]


        if k == "byr":
            if int(v) < 1920 or int(v) > 2002:
                bad = 1

        if k == "iyr":
            if int(v) < 2010 or int(v) > 2020:
                bad = 1

        if k == "eyr":
            if int(v) < 2020 or int(v) > 2030:
                bad = 1

        if k == "hgt":
            if "cm" not in v and "in" not in v:
                bad = 1
            else:
                unit = v[-2:]
                num = int(v[:-2])
                if unit == "cm":
                    if num < 150 or num > 193:
                        bad = 1
                else:
                    if num < 59 or num > 76:
                        bad = 1

        if k == "hcl":
            if v[0] != '#':
                bad = 1
            else:
                for c in v[1:]:
                    if c not in hex:
                        bad = 1

        if k == "ecl":
            if v not in hcl:
                bad = 1

        if k == "pid":
            if len(v) != 9:
                bad = 1

            for c in v:
                if c not in nums:
                    bad = 1

    if not bad:
        total += 1

print(total)
