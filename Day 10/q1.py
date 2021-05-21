import pandas as pd
import numpy as np

puzzle = [int(x) for x in open("input.txt").read().strip().split("\n")]
puzzle.sort(reverse=True)


def solve(puzzle: list):
    jolt_diff = [1, 0, 1]

    adapter1 = puzzle.pop()
    while puzzle:
        adapter2 = puzzle.pop()
        jolt_diff[(adapter2 - adapter1) - 1] += 1
        adapter1 = adapter2

    print(jolt_diff)
    return jolt_diff


j_one, _, j_three = solve(puzzle=puzzle)
print(j_one * j_three)
