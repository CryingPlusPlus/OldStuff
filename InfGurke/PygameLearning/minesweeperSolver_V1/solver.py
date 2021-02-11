class Solver:
    def __init__(self, map):
        self.map = map
        self.compass = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1))
        self.possMap = []
        self.setPossMap()
        self.oneTurn = False

    def setPossMap(self):
        self.possMap = []
        for y in range(self.map.size[1]):
            row = []
            for x in range(self.map.size[0]):
                row.append(100)
            self.possMap.append(row)

    def getPoss(self):
        for y in range(self.map.size[1]):
            for x in range(self.map.size[0]):
                if self.map.map[y][x].clicked:
                    value = self.map.map[y][x].value
                    notClicked = []
                    mines = 0
                    for comp in self.compass:
                        if 0 <= x + comp[0] < self.map.size[0] and 0 <= y + comp[1] < self.map.size[1]:
                            if not self.map.map[y + comp[1]][x + comp[0]].clicked:
                                if not self.map.map[y + comp[1]][x + comp[0]].marked:
                                    notClicked.append((x + comp[0], y + comp[1]))
                            if self.map.map[y + comp[1]][x + comp[0]].marked:
                                mines += 1
                    value -= mines
                    if len(notClicked) > 0:
                        poss = value / len(notClicked)
                    else:
                        poss = 100

                    for feld in notClicked:
                        if self.possMap[feld[1]][feld[0]] > poss:
                            self.possMap[feld[1]][feld[0]] = poss
        self.clickFeldMine()
        

    def clickFeldMine(self):
        for y, row in enumerate(self.possMap):
            for x, feld in enumerate(row):
                if feld == 0:
                    #if not self.map.map[y][x].marked:
                    #    self.map.map[y][x].marked = True
                    self.map.map[y][x].clicked = True
        '''for y in range(self.map.size[1]):
            for x in range(self.map.size[0]):
                if self.possMap[y][x] == 0:
                    self.map.feldClicked((x, y))
                if self.possMap[y][x] == 1:
                    if not self.map.map[y][x].marked:
                        self.map.feldMarked((x, y))'''
