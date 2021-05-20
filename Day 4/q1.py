import sys

passports = []

cats = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

f = set()
valid = 0

for line in sys.stdin:
    if line == "\n":
        print(f)
        if (
            len(f.intersection(cats)) == 8
            or len(f.intersection(cats)) == 7
            and "cid" not in f
        ):
            valid += 1
            print("here")
        f = set()
    else:
        v = line.split(" ")
        for i in v:
            l, r = i.split(":")
            f.add(l)

print(valid)
