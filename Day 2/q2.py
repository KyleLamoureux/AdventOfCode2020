import sys

result = 0

for line in sys.stdin:
    rnge, char, password = line.replace(":", "").split(" ")
    c_min, c_max = rnge.split("-")
    case1 = False if password[int(c_min)-1] == char else True
    case2 = False if password[int(c_max)-1] == char else True
    result = result + 1 if (case1 and not case2) or (not case1 and case2) else result

print(result)