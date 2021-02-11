import pygame
import random


class Apple:
    def __init__(self, snake):
        self.snake = snake
        self.pos = (self.snake.pos[0][0] - 10, self.snake.pos[0][1])
        self.width = self.snake.width
        self.mapSize = snake.mapSize

    def eaten(self):
        free = []
        for y in range(self.mapSize[1]):
            for x in range(self.mapSize[0]):
                if (x, y) not in self.snake.pos:
                    free.append((x, y))
        self.pos = random.choice(free)

    def draw(self, win):
        pygame.draw.rect(win, (255,0,0), (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))