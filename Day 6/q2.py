puzzle = open('input.txt').read().strip().split('\n\n')

total = 0

res = [0]*26
DIFF = 97

for line in puzzle:
    for group in line.split("\n"):
        for x in group:
            res[ord(x)- DIFF] += 1
    yes = 0
    lgh = len(line.split("\n"))
    for idx in res:
        if idx == lgh:
            yes+=1
    total += yes
    res = [0]*26

print("total: ", total)