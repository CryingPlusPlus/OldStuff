def valid(line):
    rule, pwd = line.split(": ")
    rule, char = rule.split(" ")
    mini, maxi = rule.split("-")
    
    if (pwd[int(mini) - 1] == char and pwd[int(maxi) - 1] != char) or (pwd[int(mini) - 1] != char and pwd[int(maxi) - 1] == char):
        return True
    
    return False

with open('data.txt', 'r') as fh:
    count = 0

    for line in fh:
        if valid(line):
            count += 1
    
    print(count)