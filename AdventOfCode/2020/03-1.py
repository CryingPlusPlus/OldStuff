r = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

erg = 1
for rule in r:
    with open('data.txt', 'r') as fh:
        pos = 0
        counter = 0
        for i, line in enumerate(fh):
            if i % rule[1] == 0:
                line = line.split('\n')[0]
                if line[pos % len(line)] == '#':
                    counter += 1
                pos += rule[0]
    erg *= counter
    print(counter)
print(erg)

        
