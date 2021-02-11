def valid(passport):
    codes = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

    for c in codes:
        if c not in passport:
            return False
    return True

def joiner(fh):
    out = []
    cout = []
    for line in fh:
        line = line.split('\n')[0]
        if line == "":
            out.append(''.join(cout))
            cout = []
        else:
            cout.append(line)
    
    
    out.append(''.join(cout))
    cout = []
    return out



with open('data.txt', 'r') as fh:
    pps = joiner(fh)

    counter = 0
    for p in pps:
        if valid(p):
            counter += 1
    
    print(counter)
        
