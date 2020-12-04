import sys

passports = []

cats = {'byr', 'iyr','eyr','hgt','hcl','ecl','pid','cid'}

f = set()
valid = 0

def conditions(case, value):
    if case == 'byr':
        return True if 1920 <= int(value) <= 2002 else False
    elif case == 'iyr':
        return True if 2010 <= int(value) <= 2020 else False
    elif case == 'eyr':
        return True if 2020 <= int(value) <= 2030 else False
    elif case == 'hgt':
        if value[-2:] == 'cm':
            return True if 150 <= int(value[:-2]) <= 193 else False
        elif value[-2:] == 'in':
            return True if 59 <= int(value[:-2]) <= 76 else False
    elif case == 'hcl':
        return True if value[0] == '#' and len(value) == 7 and isHcl(value[1:]) else False
    elif case == 'ecl':
        return True if value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"} else False
    elif case == 'pid':
        return True if len(value) == 9 else False
    elif case == 'cid':
        return True

def isHcl(v):
    for c in v:
        if c not in {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}:
            return False
    return True

for line in sys.stdin:
    if line == '\n':
        if len(f.intersection(cats)) == 8 or len(f.intersection(cats)) == 7 and 'cid' not in f:
            valid+=1
        f = set()
    else:
        v = line.split(' ')
        for i in v:
            l, r = i.replace('\n', '').split(':')
            if conditions(l, r):
                f.add(l)

print(valid)