import sys
from functools import reduce

OPEN = "."
TREE = "#"

x, y = 0, 0
found_trees = 0
field = []


def traverse(values):
    while values[1] < length:
        values[0] = (values[0] + values[2]) % width
        values[1] += values[3]
        values[4] = values[4] + 1 if field[values[1]][values[0]] == TREE else values[4]

    return values[-1:]


field = open("input.txt").read().strip().split("\n")

width = len(field[0])
length = len(field) - 1

# x, y, r, d, count
paths = [
    [0, 0, 1, 1, 0],
    [0, 0, 3, 1, 0],
    [0, 0, 5, 1, 0],
    [0, 0, 7, 1, 0],
    [0, 0, 1, 2, 0],
]

total = []
for p in paths:
    total.append(traverse(p)[0])

print(reduce(lambda x, y: x * y, total))
