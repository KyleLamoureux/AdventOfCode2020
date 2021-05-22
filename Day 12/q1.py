puzzle = [(x[0], int(x[1:])) for x in open("input.txt").read().strip().split("\n")]

facing = 0
x = 0
y = 0


def manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for command, val in puzzle:
    if command == "N":
        y += val
    elif command == "S":
        y -= val
    elif command == "E":
        x += val
    elif command == "W":
        x -= val
    elif command == "L":
        facing = abs(360 + facing + val) % 360
    elif command == "R":
        facing = abs(360 + facing - val) % 360
    elif command == "F":
        if facing == 0:
            x += val
        elif facing == 90:
            y += val
        elif facing == 180:
            x -= val
        elif facing == 270:
            y -= val
        else:
            print("Categories to broad...")
    else:
        print("Shouldn't be here")

print(manhattan_distance(0, x, 0, y))
