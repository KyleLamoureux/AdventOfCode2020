import sys

result = 0

for line in sys.stdin:
    rnge, char, password = line.replace(":", "").split(" ")
    c_min, c_max = rnge.split("-")
    result = result + 1 if int(c_min) <= password.count(char) <= int(c_max) else result

print(result)
