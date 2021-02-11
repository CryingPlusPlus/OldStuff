class Solver:
    def __init__(self, snake):
        self.snake = snake
        self.map = []
        # self.setMap()

        self.hydra = []
        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))

    def setMap(self):
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

    def getDir(self):
        x = self.snake.apple.pos[0] - self.snake.pos[0][0]
        y = self.snake.apple.pos[0] - self.snake.pos[0][1]
        if x == 0:
            x = 1
        if y == 0:
            y = 1
        return (int(x / abs(x)), int(y / abs(y)))

    def getWay(self):
        self.setMap()
        while True:
            if len(self.hydra) <= 0:
                bestDir = self.getDir()
                bestDir = ((0, bestDir[1]), (bestDir[0], 0))
                for dir in bestDir:
                    cell = (self.snake.pos[0][0] + dir[0], self.snake.pos[0][1] + dir[1])
                    if cell not in self.snake.pos:
                        if -1 < cell[0] < self.snake.mapSize[0] and -1 < cell[1] < self.snake.mapSize[1]:
                            return [cell]
                for comp in self.compass:
                    cell = (self.snake.pos[0][0] + comp[0], self.snake.pos[0][1] + comp[1])
                    if cell not in self.snake.pos:
                        if -1 < cell[0] < self.snake.mapSize[0] and -1 < cell[1] < self.snake.mapSize[1]:
                            return [cell]
                return [(self.snake.pos[0][0] - 1, self.snake.pos[0][1])]
            # newHydra = []
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
                    self.hydra.insert(0, nH)
            # self.hydra = newHydra
