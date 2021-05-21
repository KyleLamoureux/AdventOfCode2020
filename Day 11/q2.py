import copy
import numpy as np
from collections import Counter

puzzle = np.array(
    [
        [x[i : i + 1] for i in range(0, len(x), 1)]
        for x in open("input.txt").read().strip().split("\n")
    ]
)

MAX_ROWS = len(puzzle)
MAX_COLS = len(puzzle[0])
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
FLOOR = "."
EMPTY_SEAT = "L"
FULL_SEAT = "#"


def rule_helper(pos, puzzle, r, c):
    while (
        pos[0] + r < MAX_ROWS
        and pos[1] + c < MAX_COLS
        and pos[0] + r >= 0
        and pos[1] + c >= 0
    ):
        pos[0] += r
        pos[1] += c
        if puzzle[pos[0]][pos[1]] != FLOOR:
            return 1 if puzzle[pos[0]][pos[1]] == FULL_SEAT else 0
    return 0


def rule(row_num, col_num, ref_puzzle):
    count = 0
    for r, c in DIRECTIONS:
        count += rule_helper(pos=[row_num, col_num], puzzle=ref_puzzle, r=r, c=c)
    return count


def updatePuzzle(puzzle, ref_puzzle):
    for row_num, row in enumerate(puzzle):
        for col_num, val in enumerate(row):
            if val != FLOOR:
                rule_res = rule(row_num=row_num, col_num=col_num, ref_puzzle=ref_puzzle)
                if val == FULL_SEAT and rule_res >= 5:
                    puzzle[row_num][col_num] = EMPTY_SEAT
                elif val == EMPTY_SEAT and rule_res == 0:
                    puzzle[row_num][col_num] = FULL_SEAT
    return puzzle


seat_arrangements = set()
new_puz = copy.deepcopy(puzzle)  # Yuck.
while "".join(new_puz.flatten()) not in seat_arrangements:
    seat_arrangements.add("".join(new_puz.flatten()))  # Man I like flattening like this
    new_puz = updatePuzzle(puzzle=new_puz, ref_puzzle=puzzle)
    puzzle = copy.deepcopy(new_puz)  # Yuck.

print(Counter("".join(new_puz.flatten()))[FULL_SEAT])
