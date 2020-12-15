puzzle = open('input.txt').read().strip().split('\n')

graph = {}

FIND = 'shiny gold bag'

for line in puzzle:
    key, connections = line.split('contain')
    graph[key.strip().replace('bags', 'bag')] = [(con[3:].replace('bags', 'bag').replace('.', '').strip(), int(con[:3].strip())) for con in connections.split(',') if 'no other bags' not in con]

count = 0

def contain_bag(key):
    total = 1
    if len(graph[key]) == 0:
        return total
    else:
        for sub_key in graph[key]:
            total += sub_key[1] * contain_bag(sub_key[0])
        return total

count = contain_bag(FIND)

start = graph[FIND]

print("Total: ", count-1)
