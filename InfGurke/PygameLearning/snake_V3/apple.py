import pygame
import random


class Apple:
    def __init__(self, x, y, w, winW, winH, snake):
        self.pos = (x, y)
        self.w = w
        self.color = (255, 0, 0)
        self.winWidth = winW
        self.winHeight = winH
        self.snake = snake

    def draw(self, win):
        part = self.pos
        pygame.draw.rect(win, self.color, (part[0] * self.w, part[1] * self.w, self.w, self.w))

    def snakeFree(self):
        end = []
        for y in range(self.winHeight):
            for x in range(self.winWidth):
                if (x, y) not in self.snake.pos:
                    end.append((x, y))
        return end

    def eaten(self):
        self.pos = random.choice(self.snakeFree())
