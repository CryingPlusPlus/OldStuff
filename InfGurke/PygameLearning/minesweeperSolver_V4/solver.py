import random


class Solver:
    def __init__(self, map):
        self.map = map
        self.possMap = []
        self.setPossMap()
        self.compass = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

    def setPossMap(self):
        for y in range(self.map.size[1]):
            row = []
            for x in range(self.map.size[0]):
                row.append('n')
            self.possMap.append(row)

    def getPossMap(self):
        for y, row in enumerate(self.map.map):
            for x, feld in enumerate(row):
                if feld.clicked:
                    notClicked = []
                    value = feld.value
                    marked = 0
                    for comp in self.compass:
                        if 0 <= x + comp[0] < self.map.size[0] and 0 <= y + comp[1] < self.map.size[1]:
                            if not self.map.map[y + comp[1]][x + comp[0]].clicked:
                                if not self.map.map[y + comp[1]][x + comp[0]].marked:
                                    notClicked.append((x + comp[0], y + comp[1]))
                            if self.map.map[y + comp[1]][x + comp[0]].marked:
                                marked += 1

                    value -= marked
                    if len(notClicked) > 0:
                        poss = value / len(notClicked)
                    else:
                        poss = 'n'

                    for f in notClicked:
                        if self.possMap[f[1]][f[0]] == 'n':
                            self.possMap[f[1]][f[0]] = poss
                        else:
                            if poss == 1:
                                self.possMap[f[1]][f[0]] = poss
                            elif self.possMap[f[1]][f[0]] != 1 and self.possMap[f[1]][f[0]] > poss:
                                self.possMap[f[1]][f[0]] = poss

    def getTotalPoss(self, cell):
        totalPoss = 0
        for comp in self.compass:
            if 0 <= cell[0] + comp[0] < self.map.size[0] and 0 <= cell[1] + comp[1] < self.map.size[1]:
                x = cell[0] + comp[0]
                y = cell[1] + comp[1]
                value = self.map.map[y][x].value
                notClicked = 0
                mines = 0
                for comp in self.compass:
                    if 0 <= x + comp[0] < self.map.size[0] and 0 <= y + comp[1] < self.map.size[1]:
                        if not self.map.map[y + comp[1]][x + comp[0]].clicked and not self.map.map[y + comp[1]][
                            x + comp[0]].marked:
                            notClicked += 1
                        if self.map.map[y + comp[1]][x + comp[0]].marked:
                            mines += 1
                value -= mines
                totalPoss += value / notClicked
        # print(totalPoss)
        return totalPoss

    def clickClose(self):
        close = []
        for y, row in enumerate(self.possMap):
            for x, poss in enumerate(row):
                if poss != 'n':
                    if not self.map.map[y][x].clicked and not self.map.map[y][x].marked:
                        close.append([poss, (x, y)])

        if len(close) > 0:
            biggest = [close[0]]
            smallest = [close[0]]
            for el in close:
                if biggest[0][0] < el[0]:
                    biggest = [el]
                if biggest[0][0] == el[0]:
                    biggest.append(el)
                if smallest[0][0] > el[0]:
                    smallest = [el]
                if smallest[0][0] == el[0]:
                    smallest.append(el)
                # print('biggest', biggest)
                # print('smallest', smallest)
                # if abs(0 - smallest[0][0]) < abs(1 - biggest[0][0]):
            for el in smallest:
                el[0] = self.getTotalPoss(el[1])
            realSmall = smallest[0]
            for el in smallest:
                if el[0] < realSmall[0]:
                    realSmall = el
            self.map.feldClicked(realSmall[1])
            '''else:
                for el in biggest:
                    el[0] = self.getTotalPoss(el[1])
                realBiggest = biggest[0]
                for el in smallest:
                    if el[0] > realBiggest[0]:
                        realBiggest = el
                self.map.feldClicked(realBiggest[1])
'''
            return True
        else:
            return False

    def checkWin(self):
        for y, row in enumerate(self.map.map):
            for x, feld in enumerate(row):
                if feld.mine and not feld.marked:
                    return False
                if not feld.mine and feld.marked:
                    return False
        return True

    def clickRandom(self):
        free = []
        for y, row in enumerate(self.map.map):
            for x, feld in enumerate(row):
                if not feld.clicked and not feld.marked:
                    free.append((x, y))
        if len(free) > 0:
            feld = random.choice(free)
            self.map.feldClicked(feld)
            return True
        else:
            return False

    def clicking(self):
        if not self.map.won:
            if self.map.alive:
                self.setPossMap()
                change = False
                self.getPossMap()

                for y, row in enumerate(self.possMap):
                    for x, poss in enumerate(row):
                        if poss == 1 and not self.map.map[y][x].marked:
                            self.map.feldMarked((x, y))
                            change = True
                        if poss == 0 and not self.map.map[y][x].clicked:
                            self.map.feldClicked((x, y))
                            change = True
                #if not change:
                #    if not self.clickClose():
                #        self.clickRandom()
                if self.checkWin():
                    self.map.won = True
