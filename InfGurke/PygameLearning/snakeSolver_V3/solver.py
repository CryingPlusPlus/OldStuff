import gc


class Solver:
    def __init__(self, snake):
        self.snake = snake
        self.map = []
        # self.setMap()

        self.hydra = []
        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))
        #gc.enable()

    '''def setMap(self):
        self.map = []
        self.hydra = [[self.snake.pos[0]]]
        for y in range(self.snake.mapSize[1]):
            row = []
            for x in range(self.snake.mapSize[0]):
                if (x, y) in self.snake.pos:
                    row.append(True)
                else:
                    row.append(False)
            self.map.append(row)

    def getWay(self):
        self.setMap()
        while True:
            if len(self.hydra) <= 0:
                for comp in self.compass:
                    cell = (self.snake.pos[0][0] + comp[0], self.snake.pos[0][1] + comp[1])
                    if cell not in self.snake.pos:
                        return [cell]
                return [(self.snake.pos[0][0] - 1, self.snake.pos[0][1])]
            for head in self.hydra:
                newHeads = []
                for comp in self.compass:
                    cell = (head[-1][0] + comp[0], head[-1][1] + comp[1])
                    if -1 < cell[0] < self.snake.mapSize[0] and -1 < cell[1] < self.snake.mapSize[1]:
                        if cell not in self.snake.pos:
                            if not self.map[cell[1]][cell[0]]:
                                self.map[cell[1]][cell[0]] = True
                                newHead = head.copy()
                                newHead.append(cell)
                                newHeads.append(newHead)
                                if cell == self.snake.apple.pos:
                                    newHead.pop(0)
                                    return newHead
                self.hydra.remove(head)
                for nH in newHeads:
                    self.hydra.append(nH)'''

    def getMap(self, snake):
        map = []
        for y in range(self.snake.mapSize[1]):
            row = []
            for x in range(self.snake.mapSize[0]):
                if (x, y) in snake:
                    row.append(True)
                else:
                    row.append(False)
            map.append(row)
        return map

    def getWay(self):
        hydra = [([self.snake.pos[0]], self.getMap(self.snake.pos))]
        if len(self.hydra) <= 0:
            for comp in self.compass:
                cell = (self.snake.pos[0][0] + comp[0], self.snake.pos[0][1] + comp[1])
                if cell not in self.snake.pos:
                    return [cell]
            return [(self.snake.pos[0][0] - 1, self.snake.pos[0][1])]
        while True:
            newHydra = []
            for head in hydra:
                pWay = head[0]
                pMap = head[1]
                newHeads = []
                for comp in self.compass:
                    cell = (pWay[-1][0] + comp[0], pWay[-1][1] + comp[1])
                    if -1 < cell[0] < self.snake.mapSize[0] and -1 < cell[1] < self.snake.mapSize[1]:
                        if cell not in self.snake.pos:
                            if not pMap[cell[1]][cell[0]]:
                                pMap[cell[1]][cell[0]] = True
                                newWay = pWay.copy()
                                newWay.append(cell)
                                newHeads.append((newWay, pMap))
                                if cell == self.snake.apple.pos:
                                    newWay.pop(0)
                                    return newWay
                for nH in newHeads:
                    newHydra.append(nH)
            hydra = newHydra
