import pygame
import random


class Maze:
    def __init__(self, mazeLayer):
        self.mazeArray = []
        self.state = 'create'
        self.mLayer = mazeLayer
        self.mLayer.fill((0, 0, 0, 0))  # fill it with black translucent
        for y in range(60):
            pygame.draw.line(self.mLayer, (0, 0, 0, 255), (0, y * 8), (640, y * 8))
            for x in range(80):
                self.mazeArray.append(0x0000)
                if (y == 0):
                    pygame.draw.line(self.mLayer, (0, 0, 0, 255), (x * 8, 0), (x * 8, 480))
        self.totalCells = 4800
        self.cellStack = []

        self.currentCell = random.randint(0, self.totalCells - 1)
        self.compass = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.visitedCells = 1

    def update(self):
        if self.state == 'create':
            print('hello')

    def draw(self, screen):
        screen.blit(self.mLayer, (0, 0))
