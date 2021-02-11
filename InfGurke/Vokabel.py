vokabel = []

fh = open('Vokabel.txt', 'r')
for line in fh:
    vokabel.append(line.split(';'))
fh.close();
print(vokabel)