puzzle = open("input.txt").read().strip().split("\n")

graph = {}

FIND = "shiny gold bag"

for line in puzzle:
    key, connections = line.split("contain")
    graph[key.strip().replace("bags", "bag")] = [
        con[3:].replace("bags", "bag").replace(".", "").strip()
        for con in connections.split(",")
        if "no other bags" not in con
    ]

count = 0


def contain_bag(key):
    total = 0
    if key not in graph.keys():
        return 0
    elif key == FIND:
        return 1
    else:
        for sub_key in graph[key]:
            total += contain_bag(sub_key)
            if total > 0:
                break
        return total


for k in graph.keys():
    if k != FIND:
        count = count + 1 if contain_bag(k) > 0 else count

print("Total: ", count)
