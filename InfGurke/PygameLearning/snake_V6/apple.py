import pygame
import random

class Apple:
    def __init__(self, pos, w, snake, mapSize):
        self.pos = pos
        self.width = w
        self.snake = snake
        self.mapSize = mapSize

    def eaten(self):
        free = []
        for x in range(self.mapSize[0]):
            for y in range(self.mapSize[1]):
                if (x, y) not in self.snake.pos:
                    free.append((x, y))
        self.pos = random.choice(free)

    def draw(self, win):
        pygame.draw.rect(win, (255,0,0), (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))
