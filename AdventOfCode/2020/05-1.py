
def find_row(low, up, line):
    if len(line) == 0:
        return low
    
    mid = (low + up) // 2

    if line[0] in 'FL':
        return find_row(low, mid, line[1:])
    else:
        return find_row(mid + 1, up, line[1:])

with open('data.txt', 'r') as fh:
    l = []
    for line in fh:
        line = line.split('\n')[0]
        row = find_row(0, 127, line[:7])
        col = find_row(0, 7, line[7:])
        l.append(row * 8 + col)

print(max(l))

#Part two

mySeat = []
for i in range(max(l)):
    poss = i
    if poss not in l and poss - 1 in l and poss + 1 in l:
        mySeat.append(poss)
print(mySeat)