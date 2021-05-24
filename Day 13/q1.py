import numpy as np
import copy

time, buses = [x for x in open("input.txt").read().strip().split("\n")]
time = int(time)
buses = np.array([int(x) for x in buses.split(",") if x != "x"])
loops = copy.deepcopy(buses)

while any(ele <= time for ele in buses):
    buses = [x + loops[idx] if x < time else x for idx, x in enumerate(buses)]

val = buses - np.array([time] * len(buses))
print(loops[np.argmin(val)] * min(val))
