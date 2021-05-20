import sys
import pandas as pd
from itertools import product

values = []
for line in sys.stdin:
    values.append(int(line))

# Refreshing my memory on the old DataFrame operations. This is horribly inefficient
df = pd.DataFrame({"r1": values, "r2": values, "r3": values})
temp = [list(df[i].unique()) for i in df.columns]
df = pd.DataFrame(product(*temp), columns=df.columns)
df.drop_duplicates(inplace=True)
df["sum"] = df.sum(axis=1)
v = df.loc[df["sum"] == 2020].iloc[0]
print("{}".format(v["r1"] * v["r2"] * v["r3"]))
