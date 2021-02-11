import time, sys, random

map = []

width = 6
height = 6

compass = ((1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (-1, 0), (1, 0))


def aliveCell(cell):
    neigh = 0
    for dir in compass:
        x = cell[0] + dir[0]
        y = cell[1] + dir[1]

        if (0 <= x < width and 0 <= y < height) and map[y][x] == '#':
            neigh += 1
    alive = False
    if map[cell[1]][cell[0]] == '#' and (2 <= neigh <= 3):
        alive = True
    if map[cell[1]][cell[0]] == ' ' and neigh == 3:
        alive = True

    return alive


for y in range(height):
    nextCol = []
    for x in range(width):
        if random.randint(0, 1) == 1:
            nextCol.append('#')
        else:
            nextCol.append(' ')
    map.append(nextCol)

control_map = map.copy()

while True:

    for col in map:
        print(col)

    for x in range(width):
        for y in range(height):
            if aliveCell([x, y]):
                control_map[y][x] = '#'
            else:
                control_map[y][x] = ' '

    map = control_map.copy()

    print('\n')
    time.sleep(2.5)
