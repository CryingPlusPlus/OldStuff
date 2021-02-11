import pygame
import gc


class Solver:
    def __init__(self, snake):
        self.snake = snake
        self.mapSize = self.snake.mapSize
        self.width = self.snake.width

        self.map = []
        self.setMap()
        gc.enable()
        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))

        self.hydra = [[self.snake.pos[0]]]
        self.way = self.findWay()
        self.formatWay()

    def setMap(self):
        for y in range(self.mapSize[1]):
            nextRow = []
            for x in range(self.mapSize[0]):
                nextRow.append(False)
            self.map.append(nextRow)
        for part in self.snake.pos:
            self.map[part[1]][part[0]] = True

    def draw(self, win):
        # for head in self.hydra:
        for part in self.way:
            pygame.draw.rect(win, (0, 0, 255), (part[0] * self.width, part[1] * self.width, self.width, self.width))

    def findWay(self):
        self.setMap()
        while True:
            for head in self.hydra:
                for comp in self.compass:
                    x = head[-1][0] + comp[0]
                    y = head[-1][1] + comp[1]
                    if -1 < x < self.mapSize[0] and -1 < y < self.mapSize[1]:
                        if not self.map[y][x]:
                            self.map[y][x] = True
                            newHead = head.copy()
                            newHead.append((x, y))
                            if (x, y) == self.snake.apple.pos:
                                self.hydra = []
                                return newHead
                            self.hydra.append(newHead)
                self.hydra.remove(head)

    def formatWay(self):
        comps = []
        for i in range(1, len(self.way)):
            lpart = self.way[i - 1]
            npart = self.way[i]
            nextComp = (npart[0] - lpart[0], npart[1] - lpart[1])
            comps.append(nextComp)
        print(comps)
        self.way = comps