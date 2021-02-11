map = [[8, 5, 4, 0, 6, 9, 0, 7, 0],
       [0, 0, 0, 5, 0, 0, 0, 0, 4],
       [0, 0, 0, 0, 0, 4, 0, 0, 5],
       [9, 0, 1, 7, 0, 0, 0, 4, 0],
       [4, 0, 0, 0, 9, 0, 0, 0, 3],
       [0, 2, 0, 0, 0, 3, 9, 0, 8],
       [6, 0, 0, 8, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 6, 0, 0, 0],
       [0, 4, 0, 3, 7, 0, 1, 6, 9]]

grids = [((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)),
         ((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)),
         ((0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)),
         ((3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)),
         ((3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)),
         ((3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)),
         ((6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)),
         ((6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)),
         ((6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8))]

cols = [((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)),
        ((0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)),
        ((0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)),
        ((0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)),
        ((0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)),
        ((0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)),
        ((0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)),
        ((0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)),
        ((0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8))]

rows = [((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)),
        ((1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)),
        ((2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)),
        ((3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)),
        ((4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)),
        ((5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)),
        ((6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)),
        ((7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)),
        ((8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8))]


def getgrid(cell):
    for i in range(len(grids)):
        if cell in grids[i]:
            return i


def getrow(cell):
    for i in range(len(rows)):
        if cell in rows[i]:
            return i


def getcol(cell):
    for i in range(len(cols)):
        if cell in cols[i]:
            return i


def checkgrid(cell):
    end = []
    for i in range(1, 10):
        inthere = False
        for checkCell in grids[getgrid(cell)]:
            if map[checkCell[0]][checkCell[1]] == i:
                inthere = True
        if not inthere:
            end.append(i)

    return end


def checkrow(cell):
    end = []
    for i in range(1, 10):
        inthere = False
        for checkCell in rows[getrow(cell)]:
            if map[checkCell[0]][checkCell[1]] == i:
                inthere = True
        if not inthere:
            end.append(i)

    return end


def checkcol(cell):
    end = []
    for i in range(1, 10):
        inthere = False
        for checkCell in cols[getcol(cell)]:
            if map[checkCell[0]][checkCell[1]] == i:
                inthere = True
        if not inthere:
            end.append(i)

    return end


def getPoss(cell):
    end = []
    colnums = checkcol(cell)
    rownums = checkrow(cell)
    gridnums = checkgrid(cell)

    for i in range(1, 10):
        if i in colnums and i in rownums and i in gridnums:
            end.append(i)

    return end


def getFree():
    end = []
    for y in range(9):
        for x in range(9):
            if map[y][x] == 0:
                end.append((y, x))
    return end


def solver(checkList, state, i):
    while True:
        if state < len(checkList):
            cCell = checkList[state]
            poss = getPoss(cCell)
            trial = map[cCell[0]][cCell[1]]
            while True:
                trial += 1
                if trial in poss:
                    print(i)
                    map[cCell[0]][cCell[1]] = trial
                    state += 1
                    i += 1
                    break
                elif trial > 9:
                    print(i)
                    map[cCell[0]][cCell[1]] = 0
                    state -= 1
                    i += 1
                    break
        else:
            break


solver(getFree(), 0, 0)

for y in range(9):
    print(map[y])
