import pygame

class feld:

    def __init__(self, x, y, pos_x, pos_y, width, height, win):
        self.x = x
        self.y = y
        self.pos_x = pos_x
        self.pos.y = pos_y
        self.width = width
        self.height = height
        self.win = win

    def show(self):
        pygame.draw.rect(win, (51, 51, 51), (self.x, self.y, self.width, self.height))
        