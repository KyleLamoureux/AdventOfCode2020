import copy

puzzle = [(x1, int(x2)) for x1, x2 in [y.split(' ') for y in open('input.txt').read().strip().split('\n')]]

def solve(puzzle):
    index=0
    visited=[]
    accumulator=0
    
    while index not in visited and index < len(puzzle):
        visited.append(index)
        pos = puzzle[index]
        if pos[0] == "nop":
            index += 1
        elif pos[0] == "jmp":
            index += pos[1]
        else: #acc
            accumulator += pos[1]
            index +=1
        # print(f"{pos[0]} {pos[1]}  |  {accumulator}")
    
    return accumulator, visited, False if index in visited else True
    
def callSolve(cmd):
    new =  copy.deepcopy(puzzle)
    new[i] = (cmd, puzzle[i][1])
    ans, _, correct = solve(new)
    # print(new)
    # print(solve(new))
    if correct:
        print(f"Accumulator: {ans}")
        return True
    return False

_, visited, _ = solve(puzzle) # Find the infinite loop

for i in visited[::-1]: # Search for fix in reverse order
    if puzzle[i][0] == "nop":
        if callSolve("jmp"):
            break
    elif puzzle[i][0] == "jmp": 
        if callSolve("nop"):
            break