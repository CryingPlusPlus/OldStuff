import pygame
from snake_V4.feld import Feld


class Map:
    def __init__(self, mapsize, feldw):
        self.mapSize = mapsize
        self.feldWidth = feldw
        self.map = []
        for y in range(self.mapSize[1]):
            nextrow = []
            for x in range(self.mapSize[0]):
                nextrow.append(Feld((x * self.feldWidth, y * self.feldWidth), self.feldWidth))
            self.map.append(nextrow)

    def glow(self, win, color, cell):
        self.map[cell[1]][cell[0]].glow(win, color)

    def fill(self, win, comp, fcolor, bcolor, cell):
        return self.map[cell[1]][cell[0]].fill(win, comp, fcolor, bcolor)

    def updateVel(self, newVel):
        for row in self.map:
            for feld in row:
                feld.vel = newVel


