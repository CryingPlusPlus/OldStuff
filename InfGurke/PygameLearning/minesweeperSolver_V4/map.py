from minesweeperSolver_V4.feld import Feld
import pygame
import random
import time


class Map:
    def __init__(self, size, w, minePoss, font):
        self.size = size
        self.feldwidth = w
        self.minePoss = minePoss
        self.font = font
        self.compass = ((-1, -1), (1, -1), (1, 1), (-1, 1), (0, -1), (1, 0), (0, 1), (-1, 0))

        self.map = []
        self.setMap()
        self.alive = True
        self.won = False

    def checkWin(self):
        for row in self.map:
            for feld in row:
                if (feld.mine and not feld.clicked) or (not feld.mine and feld.marked):
                    return False
        return True

    def firstClick(self, pos):
        self.map[pos[1]][pos[0]].mine = False
        for comp in self.compass:
            if 0 <= pos[0] + comp[0] < self.size[0] and 0 <= pos[1] + comp[1] < self.size[1]:
                self.map[pos[1] + comp[1]][pos[0] + comp[0]].mine = False
        self.setValues()
        self.setText()
        self.feldClicked(pos)

    def setMap(self):

        for y in range(self.size[1]):
            nextRow = []
            for x in range(self.size[0]):
                m = self.font.render('F', True, (27, 92, 90), (47, 140, 150))
                mr = m.get_rect()
                mr.center = (x * self.feldwidth + self.feldwidth / 2, y * self.feldwidth + self.feldwidth / 2)
                nextRow.append(Feld((x, y), self.feldwidth, self.font, m, mr, self))
            self.map.append(nextRow)

    def draw(self, win):

        pygame.draw.line(win, (51, 51, 51), (0, 0), (self.size[0] * self.feldwidth, 0))
        pygame.draw.line(win, (51, 51, 51), (0, 0), (0, self.size[1] * self.feldwidth))
        for row in self.map:
            for feld in row:
                feld.draw(win)

    def feldMarked(self, pos):
        if not self.map[pos[1]][pos[0]].clicked:
            if self.map[pos[1]][pos[0]].marked:
                self.map[pos[1]][pos[0]].marked = False
            else:
                self.map[pos[1]][pos[0]].marked = True
        self.checkWin()

    def feldClicked(self, pos):
        if not self.map[pos[1]][pos[0]].clicked:
            if not self.map[pos[1]][pos[0]].marked:
                self.map[pos[1]][pos[0]].clicked = True

            if self.map[pos[1]][pos[0]].value == 0:
                for comp in self.compass:
                    if 0 <= pos[0] + comp[0] < self.size[0] and 0 <= pos[1] + comp[1] < self.size[1]:
                        # self.map[pos[1] + comp[1]][pos[0] + comp[0]].clicked = True
                        self.feldClicked((pos[0] + comp[0], pos[1] + comp[1]))
                # self.map[y_cord][x_cord]...
        if self.map[pos[1]][pos[0]].mine and self.map[pos[1]][pos[0]].clicked:
            self.alive = False
        self.checkWin()

    def setMines(self):
        for row in self.map:
            for feld in row:
                if random.uniform(0, 1) <= self.minePoss:
                    feld.mine = True

    def setText(self):
        for row in self.map:
            for feld in row:
                feld.setText()

    def setValues(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                for comp in self.compass:
                    if 0 <= x + comp[0] < self.size[0] and 0 <= y + comp[1] < self.size[1]:
                        if self.map[y + comp[1]][x + comp[0]].mine:
                            self.map[y][x].value += 1
