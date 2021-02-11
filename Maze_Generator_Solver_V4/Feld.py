import pygame
from Maze import *
from __main__ import *


class feld:
    def __init__(self, feldLayer, pos_x, pos_y, seite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ways = [False, False, False, False]
        self.visited = False
        self.seite = seite
        self.x = self.pos_x * self.seite
        self.y = self.pos_y * self.seite
        self.feldLayer = feldLayer
        #self.feldLayer.fill(255, 255, 255)
        self.snake = False
        self.feld_clr = (255, 255, 255)

    def update(self):
        x = self.x
        y = self.y
        seite = self.seite
        pygame.draw.rect(self.feldLayer, self.feld_clr, (x, y, seite, seite))
        if not self.ways[0]:
            pygame.draw.line(self.feldLayer, (0,0,0), (x, y), (x + seite, y))
        if not self.ways[1]:
            pygame.draw.line(self.feldLayer, (0,0,0), (x + seite, y), (x + seite, y + seite))
        if not self.ways[2]:
            pygame.draw.line(self.feldLayer, (0,0,0), (x + seite, y + seite), (x, y + seite))
        if not self.ways[3]:
            pygame.draw.line(self.feldLayer, (0,0,0), (x, y + seite), (x, y))

    def show(self, screen):
        screen.blit(self.feldLayer, (0, 0))