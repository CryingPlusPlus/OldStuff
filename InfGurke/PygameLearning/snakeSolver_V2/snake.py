import pygame
from snakeSolver_V2.apple import Apple
from snakeSolver_V2.solver import Solver


class Snake:
    def __init__(self):
        self.pos = [(15, 15)]
        self.mapSize = (30, 30)
        self.width = 20
        self.apple = Apple(self)

        self.nextCell = (16, 15)

        self.vel = 4
        self.current = 0
        self.alive = True
        self.way = []
        self.eaten = False

        self.solver = Solver(self)

    def wallCollision(self):
        if not -1 < self.nextCell[0] < self.mapSize[0] or not -1 < self.nextCell[1] < self.mapSize[1]:
            self.alive = False

    def appleCollision(self):
        if self.nextCell == self.apple.pos:
            self.apple.eaten()
            self.eaten = True

    def move(self, win):
        self.draw(win)
        if self.alive:
            self.current += self.vel
            if self.current >= self.width:
                self.current = 0
                self.pos.insert(0, self.nextCell)
                if len(self.way) <= 0:
                    self.way = self.solver.getWay()
                self.nextCell = self.way[0]
                self.way.pop(0)
                if self.eaten:
                    self.eaten = False
                else:
                    self.pos.pop(-1)
            self.appleCollision()
            self.wallCollision()

    def draw(self, win):
        for part in self.pos:
            pygame.draw.rect(win, (0, 255, 0), (part[0] * self.width, part[1] * self.width, self.width, self.width))
        self.apple.draw(win)
