import sys

instructions = [line.strip() for line in open(sys.argv[1]).readlines()]

for i in range(len(instructions)):

    orig = instructions[i]

    if "jmp" in orig:
        new = orig.replace('jmp', 'nop')
    elif "nop" in orig:
        new = orig.replace('nop', 'jmp')
    else:
        continue

    instructions[i] = new

    seen = []

    eip = 0
    eax = 0

    while eip not in seen and eip < len(instructions):

        seen.append(eip)
        inst, amt = instructions[eip].split()

        if inst ==  'jmp':
            eip += int(amt)
        elif inst == 'acc':
            eax += int(amt)
            eip += 1
        else:
            eip += 1

    if eip == len(instructions):
        print(eax)
        break
    else:
        instructions[i] = orig
