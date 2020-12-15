puzzle = [int(x) for x in open('input.txt').read().strip().split('\n')]

TARGET_ERROR = 1124361034

def solve(index, values):
    if sum(values) >= TARGET_ERROR:
        return values
    else:
        values.append(puzzle[index])
        return solve(index+1, values)

for index in range(len(puzzle)):
    if puzzle[index] < TARGET_ERROR:
        ans = solve(index, [])
        if sum(ans) == TARGET_ERROR:
            print(f"Encryption weakness: {min(ans) + max(ans)}")
            break
