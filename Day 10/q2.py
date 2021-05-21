from collections import OrderedDict

puzzle = sorted([int(x) for x in open("input.txt").read().strip().split("\n")])
puzzle = [0] + puzzle + [max(puzzle) + 3]

graph_list = []
for val in puzzle:
    graph_list.append((val, [x for x in range(val + 1, val + 4) if x in puzzle]))

graph = OrderedDict(graph_list)


def dfs(val, memory={}):
    if val in memory:  # Memory
        return memory[val]
    elif graph[val]:  # Graph can progress deeper
        memory[val] = sum(dfs(x) for x in graph[val])
        return memory[val]
    else:  # Base case
        return 1


print(dfs(0))
