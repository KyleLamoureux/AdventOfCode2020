puzzle = [(x[0], int(x[1:])) for x in open("input.txt").read().strip().split("\n")]

facing = 0
waypoint_x = 10
waypoint_y = 1
boat_x = 0
boat_y = 0


def manhattan_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def rotate(x, y, rotation):
    if rotation == ["R", 90]:
        return [y, -x]
    elif rotation == ["L", 90]:
        return [-y, x]
    elif rotation == ["L", 180] or rotation == ["R", 180]:
        return [-x, -y]
    elif rotation == ["R", 270]:
        return [-y, x]
    elif rotation == ["L", 270]:
        return [y, -x]


for command, val in puzzle:
    if command == "N":
        waypoint_y += val
    elif command == "S":
        waypoint_y -= val
    elif command == "E":
        waypoint_x += val
    elif command == "W":
        waypoint_x -= val
    elif command in ["L", "R"]:
        waypoint_x, waypoint_y = rotate(waypoint_x, waypoint_y, [command, val])
    elif command == "F":
        boat_x += waypoint_x * val
        boat_y += waypoint_y * val
    else:
        print("Shouldn't be here")

    # print(f"Waypoint: x:{waypoint_x}, y:{waypoint_y}")
    # print(f"Boat: x:{boat_x}, y:{boat_y}\n")

print(manhattan_distance(boat_x, 0, boat_y, 0))
