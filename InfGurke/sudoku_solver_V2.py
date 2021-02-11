import gc

gc.enable()
map = [[5, 0, 0, 1, 6, 0, 0, 0, 7],
       [0, 0, 0, 0, 8, 0, 6, 0, 0],
       [7, 0, 0, 3, 0, 5, 0, 0, 0],
       [0, 0, 0, 2, 0, 0, 3, 0, 4],
       [0, 5, 4, 6, 0, 7, 8, 1, 0],
       [3, 0, 2, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 9, 0, 2, 0, 0, 5],
       [0, 0, 5, 0, 7, 0, 0, 0, 0],
       [4, 0, 0, 0, 1, 3, 0, 0, 9]]

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


def correctCell(cell):
    if map[cell[0]][cell[1]] == 0:
        end = []
        colnums = checkcol(cell)
        rownums = checkrow(cell)
        gridnums = checkgrid(cell)

        for i in range(1, 10):
            if i in colnums and i in rownums and i in gridnums:
                end.append(i)

        if len(end) == 1:
            map[cell[0]][cell[1]] = end[0]
            return True
        else:
            return False
    else:
        return False


def GridRowColIteration():
    someChange = False
    change = 1
    while change > 0:
        change = 0

        for x in range(9):
            for y in range(9):
                if correctCell((y, x)):
                    change += 1
                    someChange = True
    return someChange


def getFree():
    end = []
    for y in range(9):
        for x in range(9):
            if map[y][x] == 0:
                end.append((y, x))
    return end


def getCheckingList():
    free = getFree()
    end = []
    for cell in free:
        end.append([cell, 1])
    return end


def rec_checking(checkingList, doneList):
    while True:
        if len(checkingList) != 0:
            currentCellInfo = checkingList[-1]
            currentCell = currentCellInfo[0]
            trial = currentCellInfo[1]
            if len(getPoss(currentCell)) != 0:
                print('building')
                while True:
                    if trial in getPoss(currentCell):
                        map[currentCell[0]][currentCell[1]] = trial
                        if trial < 9:
                            currentCellInfo[1] = trial + 1
                        else:
                            currentCellInfo[1] = 1
                        checkingList.pop(-1)
                        doneList.append(currentCellInfo)
                        break
                    else:
                        if trial < 9:
                            trial += 1
                        else:
                            trial = 1
            else:
                print('popping')
                while True:
                    remCellInfo = doneList.pop(-1)
                    remCell = remCellInfo[0]
                    map[remCell[0]][remCell[1]] = 0
                    checkingList.append(remCellInfo)
                    if len(getPoss(currentCell)) != 0:
                        break

        else:
            break


GridRowColIteration()


if len(getFree()) != 0:
    rec_checking(getCheckingList(), [])

for y in range(9):
    print(map[y])
