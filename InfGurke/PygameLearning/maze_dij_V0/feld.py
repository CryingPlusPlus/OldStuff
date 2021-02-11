import pygame


class Feld:
    def __init__(self, pos, w):
        self.pos = pos
        self.width = w

        self.visited = False

        self.color = (255, 255, 255)
        self.ways = [False, False, False, False]

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))
