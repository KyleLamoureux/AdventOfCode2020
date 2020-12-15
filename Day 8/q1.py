puzzle = [(x1, int(x2)) for x1, x2 in [y.split(' ') for y in open('input.txt').read().strip().split('\n')]]

accumulator = 0
visited = set()
index = 0

while index not in visited:
    visited.add(index)
    pos = puzzle[index]
    if pos[0] == "nop":
        index += 1
    elif pos[0] == "jmp":
        index += pos[1]
    else: #acc
        accumulator += pos[1]
        index +=1
    # print(f"{pos[0]} {pos[1]}  |  {accumulator}")
    

print(f"Accumulator: {accumulator}")