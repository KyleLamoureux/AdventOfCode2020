puzzle = open("input.txt").read().strip().split("\n\n")

total = 0
anwnser = set()

for line in puzzle:
    for group in line.split("\n"):
        for x in group:
            anwnser.add(x)
    total += len(anwnser)
    anwnser = set()

print("total: ", total)
