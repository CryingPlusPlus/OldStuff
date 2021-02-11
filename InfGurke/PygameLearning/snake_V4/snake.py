import pygame
from snake_V4.map import Map
from snake_V4.apple import Apple
import time


class Snake:
    def __init__(self, mapsize, feldw, pos):
        self.map = Map(mapsize, feldw)
        self.pos = [(15, 15), (16, 15), (17, 15)]
        self.width = feldw

        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.lastcomp = self.compass[3]
        self.comps = [self.lastcomp, self.lastcomp]
        self.newComp = self.lastcomp
        self.eaten = False

        self.lastCell = (18, 15)
        self.apple = Apple((5, 15), self.map, snake=self)
        self.nextCell = self.getNextCell()

        self.alive = True

    def getNextCell(self):
        return self.pos[0][0] + self.lastcomp[0], self.pos[0][1] + self.lastcomp[1]
        # return (self.pos[0][0] + self.newComp[0], self.pos[0][1] + self.newComp[1])

    def appleEaten(self):
        if self.nextCell == self.apple.pos:
            self.eaten = True
            self.apple.eaten()

    def wallCollision(self):
        if not -1 < self.nextCell[0] < self.map.mapSize[0] or not -1 < self.nextCell[1] < self.map.mapSize[1]:
            self.alive = False

    def snakeCollision(self):
        if self.nextCell in self.pos:
            self.alive = False

    def updateVel(self, newVel):
        self.map.updateVel(newVel)

    def move(self, win, r=4):
        # time.sleep(0.016)
        if self.alive:
            self.apple.draw(win)
            self.appleEaten()
            if r == 4:
                pass
            else:
                self.newComp = self.compass[r]
                # self.lastcomp = self.compass[r]
                self.nextCell = self.getNextCell()

            frontFill = self.map.fill(win, self.lastcomp, (0, 255, 0), (51, 51, 51), self.nextCell)
            if frontFill:
                self.pos.insert(0, self.nextCell)
                self.comps.insert(0, (self.lastcomp[0], self.lastcomp[1]))
                # self.comps.insert(0, self.newComp)
                self.lastcomp = self.newComp
                self.nextCell = self.getNextCell()

                if not self.eaten:
                    self.lastCell = self.pos.pop(-1)
                    self.comps.pop(-1)
                else:
                    self.eaten = False
                for part in self.pos:
                    self.map.glow(win, (0, 255, 0), part)
            else:
                self.map.fill(win, self.comps[-1], (51, 51, 51), (0, 255, 0), self.pos[-1])
                for part in self.pos[:-1]:
                    self.map.glow(win, (0, 255, 0), part)
            self.wallCollision()
            self.snakeCollision()
        else:
            for part in self.pos:
                self.map.glow(win, (0, 255, 0), part)
                self.apple.draw(win)

    def getUpdate(self):
        end = [pygame.Rect(self.nextCell[0] * self.width, self.nextCell[1] * self.width, self.width, self.width)]

        for part in self.pos:
            end.append(pygame.Rect(part[0] * self.width, part[1] * self.width, self.width, self.width))
        end.append(pygame.Rect(self.lastCell[0] * self.width, self.lastCell[1] * self.width, self.width, self.width))
        end.append(pygame.Rect(self.apple.pos[0] * self.width, self.apple.pos[1] * self.width, self.width, self.width))

        return end
