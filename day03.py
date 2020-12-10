import sys

rows = [line.strip() for line in open(sys.argv[1])]

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

total = 1

for slope in slopes:
    trees = 0

    col = 0
    row = 0
    while row < len(rows):
        if rows[row][col] == '#':
            trees += 1

        col += slope[0]

        if col >= len(rows[0]):
            col = col % len(rows[0])

        row += slope[1]

    total *= trees

print(total)
