from itertools import product
import pandas as pd

puzzle = [int(x) for x in open('input.txt').read().strip().split('\n')]

pre = 25

def solve(target, options):
    df = pd.DataFrame({"r1":options, "r2":options})
    temp = [list(df[i].unique()) for i in df.columns]
    df = pd.DataFrame(product(*temp), columns=df.columns)
    df.drop_duplicates(inplace=True)
    df["sum"] = df.sum(axis=1)
    v = df.loc[df["sum"] == target]
    return False if len(v)==0 else True

for index, v in enumerate(puzzle[pre:]):
    # print(f"{v},{index} - {puzzle[index:pre+index]}")
    if not solve(v, puzzle[index:pre+index]):
        print(f"Found Error: {v}")
        # break
