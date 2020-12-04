import sys

values = []
for line in sys.stdin:
    convert = int(line)
    if values and 2020-convert in values:
        print((2020-convert)*(convert))
        break
    else:
        values.append(convert)