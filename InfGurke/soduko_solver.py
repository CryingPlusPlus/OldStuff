game = [[2, 0, 0, 8, 0, 3, 7, 9, 0],
        [0, 4, 0, 6, 0, 1, 0, 0, 0],
        [0, 6, 0, 0, 9, 0, 3, 4, 0],
        [0, 0, 0, 9, 1, 0, 0, 7, 0],
        [0, 0, 0, 0, 6, 0, 8, 0, 4],
        [0, 0, 0, 0, 2, 7, 0, 0, 3],
        [0, 2, 6, 0, 3, 0, 0, 0, 5],
        [0, 9, 5, 2, 0, 0, 6, 0, 0],
        [0, 0, 3, 1, 0, 6, 0, 0, 0]]

a = [[0, 0], [0, 1], [0, 2],
     [1, 0], [1, 1], [1, 2],
     [2, 0], [2, 1], [2, 2]]

b = [[0, 3], [0, 4], [0, 5],
     [1, 3], [1, 4], [1, 5],
     [2, 3], [2, 4], [2, 5]]

c = [[0, 6], [0, 7], [0, 8],
     [1, 6], [1, 7], [1, 8],
     [2, 6], [2, 7], [2, 8]]

d = [[3, 0], [3, 1], [3, 2],
     [4, 0], [4, 1], [4, 2],
     [5, 0], [5, 1], [5, 2]]

e = [[3, 3], [3, 4], [3, 5],
     [4, 3], [4, 4], [4, 5],
     [5, 3], [5, 4], [5, 5]]

f = [[3, 6], [3, 7], [3, 8],
     [4, 6], [4, 7], [4, 8],
     [5, 6], [5, 7], [5, 8]]

g = [[6, 0], [6, 1], [6, 2],
     [7, 0], [7, 1], [7, 2],
     [8, 0], [8, 1], [8, 2]]

h = [[6, 3], [6, 4], [6, 5],
     [7, 3], [7, 4], [7, 5],
     [8, 3], [8, 4], [8, 5]]

i = [[6, 6], [6, 7], [6, 8],
     [7, 6], [7, 7], [7, 8],
     [8, 6], [8, 7], [8, 8]]


def rowcheck(row, num):
    check = 0
    for zahl in game[row]:
        if zahl == num:
            check += 1
    if check == 0:
        return True
    else:
        return False


def colcheck(col, num):
    check = 0
    for i in range(9):
        if game[i][col] == num:
            check += 1
    if check == 0:
        return True
    else:
        return False


def fieldcheck(field, num):
    check = 0
    for feld in field:
        if game[feld[0]][feld[1]] == num:
            check += 1

    if check == 0:
        return True
    else:
        return False


def solve(field):
    for i in range(1, 10):
        if fieldcheck(field, i):
            pos = []
            for f in field:
                if rowcheck(f[0], i) and colcheck(f[1], i) and game[f[0]][f[1]] == 0:
                    pos.append(f)
            if pos.__len__() == 1:
                game[pos[0][0]][pos[0][1]] = i
                return True
            else:
                return False
total_change = 1

while total_change > 0:

    total_change = 0

    if solve(a):
        total_change += 1

    if solve(b):
        total_change += 1

    if solve(c):
        total_change += 1

    if solve(d):
        total_change += 1

    if solve(e):
        total_change += 1

    if solve(f):
        total_change += 1

    if solve(g):
        total_change += 1

    if solve(h):
        total_change += 1

    if solve(i):
        total_change += 1

    print(total_change)


print(h[7])
print(game[8][4])

for row in game:
    print(row)
