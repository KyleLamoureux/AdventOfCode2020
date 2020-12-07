puzzle = open('input.txt').read().strip().split('\n')

graph = {}

FIND = 'shiny gold bag'

for line in puzzle:
    key, connections = line.split('contain')
    graph[key.strip().replace('bags', 'bag')] = [(con[3:].replace('bags', 'bag').replace('.', '').strip(), int(con[:3].strip())) for con in connections.split(',') if 'no other bags' not in con]

count = 0
test = 0

def contain_bag(key, many, v):
    global test

    total = 0
    if key not in graph.keys():
        print("fuck")
        return 0
    elif len(graph[key]) == 0:
        test += 1*many
        return 1*many
    else:
        level = 0
        for sub_key in graph[key]:
            print(graph[key])
            print("-- ", sub_key[0], sub_key[1]) 
            total = contain_bag(sub_key[0], sub_key[1], v+1)*many
            if v != 0:
                test = test + total
            # + v
            # total *= graph[key][0][1]
            print("- ", total, "-- ", v)
            print("test: " , test)
        return total

# for k in graph.keys():
#     if k != FIND:
#         count = count+1 if contain_bag(k) > 0 else count

print(graph)
count = contain_bag(FIND, 1, 0)

print("Total: ", count)