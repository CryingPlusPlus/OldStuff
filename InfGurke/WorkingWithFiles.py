fh = open('WorkingWithFiles', 'r')
obst = fh.readlines()
fh.close()
print(obst)
for i in range(len(obst)):
    if '\n' in obst[i]:
        obst[i] = obst[i][:-1]

fh = open('WorkingWithFiles', 'a')
for o in obst:
    fh.write(o + '\n')
fh.close()