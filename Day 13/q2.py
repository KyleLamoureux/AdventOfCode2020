import numpy as np
import copy

# Does it work? Technically yes, just extremely slow. Have to revist this at a later date

time, buses = [x for x in open("input.txt").read().strip().split("\n")]
buses = np.array([[idx, int(x)] for idx, x in enumerate(buses.split(",")) if x != "x"])
loops = copy.deepcopy(buses)


def check_condition(buses):
    prev = buses[0]
    for idx, val in enumerate(buses[1:]):
        if val[1] - prev[1] == val[0]:
            continue
        else:
            return False
    return True


def doIncrement(buses, idx, prev):
    while buses[idx][1] <= prev:
        buses[idx][1] += loops[idx][1]


while not check_condition(buses=buses):
    buses[0][1] += loops[0][1]
    prev = buses[0][1]
    for idx, bus in enumerate(buses[1:]):
        doIncrement(buses, idx + 1, prev)
        prev = buses[idx + 1][1]

print(buses[0][1])
