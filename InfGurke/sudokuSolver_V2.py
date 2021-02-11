import math


def valid(cell, num, map):
    for i in range(9):
        if map[cell[1]][i] == num or map[i][cell[0]] == num:
            return False
    cell = (math.floor(cell[0] / 3), math.floor(cell[1] / 3))

    for y in range(3):
        for x in range(3):
            if map[cell[1] + y][cell[0] + x] == num:
                return False
    return True


def solver(free, deep, map):
    if len(free) > deep:
        i = map[free[deep][1]][free[deep][0]]
        while True:
            i += 1
            if i > 9:
                return solver(free, deep - 1, map)
            if valid(free[deep], i, map):
                map[free[deep[1]]][free[deep[0]]] = i
                return solver(free, deep + 1, map)


