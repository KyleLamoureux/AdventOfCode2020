def binary_space(array, code, position, low, high):
    mid = (high + low) // 2

    if position < len(code) - 1:
        if code[position] == "F" or code[position] == "L":
            return binary_space(array, code, (position + 1), low, (mid))
        elif code[position] == "B" or code[position] == "R":
            return binary_space(array, code, (position + 1), (mid + 1), high)
    else:
        return (
            array[mid + 1]
            if code[position] == "B" or code[position] == "R"
            else array[mid]
        )


puzzle = open("input.txt").read().strip().split("\n")

rows = list(range(0, 128))
columns = list(range(0, 8))

all_ids = list(range(99, 975))

found_ids = set()

for code in puzzle:
    row = code[:7]
    col = code[7:]
    row_a = binary_space(rows, row, 0, 0, len(rows) - 1)
    col_a = binary_space(columns, col, 0, 0, len(columns) - 1)
    found_ids.add((row_a * 8) + col_a)

print(set(all_ids) - found_ids)
