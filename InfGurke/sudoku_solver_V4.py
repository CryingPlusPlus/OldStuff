import numpy as np
import time
map = [[9, 0, 0, 0, 2, 7, 8, 0, 0],
       [0, 0, 0, 3, 0, 0, 0, 0, 0],
       [0, 6, 0, 0, 1, 9, 0, 0, 0],
       [0, 0, 0, 0, 9, 0, 1, 5, 0],
       [0, 7, 0, 0, 6, 0, 0, 0, 0],
       [0, 9, 4, 0, 8, 5, 7, 2, 0],
       [0, 0, 7, 0, 0, 4, 0, 6, 0],
       [0, 0, 9, 2, 0, 1, 3, 0, 0],
       [4, 0, 1, 0, 0, 0, 5, 0, 9]]


def valid(cell, num):
    for i in range(9):
        if map[cell[0]][i] == num or map[i][cell[1]] == num:
            return False
    for i in range(3):
        for j in range(3):
            if map[(cell[0] // 3) * 3 + i][(cell[1] // 3) * 3 + i] == num:
                return False
    return True


def freeCells():
    end = []
    for y in range(9):
        for x in range(9):
            if map[y][x] == 0:
                end.append((y, x))
    return end


def rec_solver(freeList, index):
    print(index)
    if index <= len(freeList) - 1:
        cCell = freeList[index]
        cVal = map[cCell[0]][cCell[1]]
        while True:
            cVal += 1
            if cVal > 9:
                map[cCell[0]][cCell[1]] = 0
                return rec_solver(freeList, index - 1)
            if valid(cCell, cVal):
                map[cCell[0]][cCell[1]] = cVal
                return rec_solver(freeList, index + 1)


rec_solver(freeCells(), 0)

for row in map:
    print(row)
