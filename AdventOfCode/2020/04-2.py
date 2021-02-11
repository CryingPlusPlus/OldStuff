def byr_checker(value):
    value = value.split(':')[1]
    if len(value) != 4:
        return False
    if not value.isnumeric():
        return False
    if not (0 <= int(value) - 1920 <= 2002 - 1920):
        return False

    return True

def iyr_checker(value):
    value = value.split(':')[1]
    if len(value) != 4:
        return False
    if not value.isnumeric():
        return False
    if not (0 <= int(value) - 2010 <= 2020 - 2010):
        return False

    return True

def eyr_checker(value):
    value = value.split(':')[1]
    if len(value) != 4:
        return False
    if not value.isnumeric():
        return False
    if not (0 <= int(value) - 2020 <= 2030 - 2020):
        return False

    return True

def hgt_checker(value):
    value = value.split(':')[1]

    if 'in' in value:
        value = value.split('in')[0]
        if len(value) == 0:
            return False
        if not value.isnumeric():
            return False
        if (0 <= int(value) - 59 <= 76 - 59):
            return True
    if 'cm' in value:
        value = value.split('cm')[0]
        if len(value) == 0:
            return False
        if not value.isnumeric():
            return False
        if (0 <= int(value) - 150 <= 193 - 150):
            return True
        

    return False

def hcl_checker(value):
    value = value.split(':')[1]
    v = '0123456789abcdef'
    if value[0] != '#':
        return False
    value = value.split('#')[1]
    for char in value:
        if char not in v:
            return False
    return True


def ecl_checker(value):
    value = value.split(':')[1]
    v = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if value in v:
        return True
    return False

def pid_checker(value):
    value = value.split(':')[1]
    v = '0123456789'

    if len(value) != 9:
        return False
    for char in value:
        if char not in v:
            return False
    return True


def valid(passport):
    codes = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

    for c in codes:
        if c not in passport:
            return False
    
    passport = passport.split(' ')

    for p in passport:
        if p[:4] == 'byr:':
            if not byr_checker(p):
                print('byr')
                return False
        if p[:4] == 'iyr:':
            if not iyr_checker(p):
                print('iyr')
                return False
        if p[:4] == 'eyr:':
            if not eyr_checker(p):
                print('eyr')
                return False
        if p[:4] == 'hgt:':
            if not hgt_checker(p):
                print('hgt')
                return False
        if p[:4] == 'hcl:':
            if not hcl_checker(p):
                print('hcl')
                return False
        if p[:4] == 'ecl:':
            if not ecl_checker(p):
                print('ecl')
                return False
        if p[:4] == 'pid:':
            if not pid_checker(p):
                print('pid')
                return False
        
    return True

def joiner(fh):
    out = []
    cout = []
    for line in fh:
        line = line.split('\n')[0]
        if line == "":
            out.append(' '.join(cout))
            cout = []
        else:
            cout.append(line)
    
    
    out.append(' '.join(cout))
    return out



with open('data.txt', 'r') as fh:
    pps = joiner(fh)

    counter = 0
    for p in pps:
        if valid(p):
            counter += 1
    
    print(counter)
        
