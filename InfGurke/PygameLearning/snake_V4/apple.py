import pygame
from snake_V4.map import Map
import random


class Apple:
    def __init__(self, pos, map, snake):
        self.pos = pos
        self.map = map
        self.snake = snake

    def draw(self, win):
        self.map.glow(win, (255, 0, 0), self.pos)

    def eaten(self):
        free = []
        for x in range(1, self.map.mapSize[0]-1):
            for y in range(1, self.map.mapSize[1]-1):
                if not (x, y) in self.snake.pos:
                    free.append((x, y))

        self.pos = random.choice(free)
