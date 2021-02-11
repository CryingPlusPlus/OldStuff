def valid(line):
    rule, pwd = line.split(": ")
    rule, char = rule.split(" ")
    mini, maxi = rule.split("-")

    count = 0
    for el in pwd:
        if el == char:
            count += 1
    if int(mini) <= count <= int(maxi):
        return True
    
    return False


with open('data.txt', 'r') as fh:
    count = 0
    for line in fh:
        if valid(line):
            count += 1
    
    print(count)