inp = [15,12,0,14,3,1]

indicies = {}

for i in range(len(inp) - 1):
    indicies[inp[i]] = i + 1

end = 30000000
curr = len(inp)

prev = inp[-1]

while curr < end:
    if prev not in indicies:
        indicies[prev] = curr
        prev = 0
    else:
        old = indicies[prev]
        indicies[prev] = curr
        prev = curr-old

    curr += 1

print(prev)
