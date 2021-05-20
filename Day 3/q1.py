import sys

OPEN = "."
TREE = "#"

x, y = 0, 0
found_trees = 0
field = []

field = open("input.txt").read().strip().split("\n")

width = len(field[0])
length = len(field) - 1

while y < length:
    x = (x + 3) % width
    y += 1
    found_trees = found_trees + 1 if field[y][x] == TREE else found_trees

print(found_trees)
