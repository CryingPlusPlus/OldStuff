import pygame
from snakeSolver_V1.apple import Apple


class Snake:

    def __init__(self, pos, w, mapSize):
        self.pos = [pos]
        self.width = w
        self.mapSize = mapSize
        self.apple = Apple((5, 15), self)

        self.vel = 4
        self.current = 0

        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.lastcomp = self.compass[3]

        self.alive = True
        self.eaten = False

        self.nextCell = None
        self.getNextCell()

    def getNextCell(self):
        self.nextCell = (self.pos[0][0] + self.lastcomp[0], self.pos[0][1] + self.lastcomp[1])

    def appleCollision(self):
        if self.nextCell == self.apple.pos:
            self.eaten = True

    def draw(self, win):
        for part in self.pos:
            pygame.draw.rect(win, (0, 255, 0), (part[0] * self.width, part[1] * self.width, self.width, self.width))

    def wallCollision(self):
        if not -1 < self.nextCell[0] < self.mapSize[0] or not -1 < self.nextCell[1] < self.mapSize[1]:
            self.alive = False

    def snakeCollision(self):
        if self.nextCell in self.pos:
            self.alive = False

    def move(self, win, r=4):
        if self.alive:
            if r < 4:
                if self.compass[r] != self.lastcomp:
                    self.lastcomp = self.compass[r]

            if self.current < self.width:
                self.current += self.vel
            else:

                self.current = 0
                self.pos.insert(0, self.nextCell)
                self.getNextCell()
                if self.eaten:
                    self.eaten = False
                    self.apple.eaten()
                else:
                    self.pos.pop(-1)

        self.draw(win)
        self.apple.draw(win)
        self.appleCollision()
        self.wallCollision()
        self.snakeCollision()
