import pygame
from snake_V6.apple import Apple


class Snake:
    def __init__(self, mapSize):
        self.pos = [(15, 15)]
        self.width = 20
        self.mapSize = mapSize

        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.lastcomp = self.compass[3]
        self.comps = [self.lastcomp, self.lastcomp]
        self.nextCell = (14, 15)
        self.endCell = (16, 15)

        self.apple = Apple((5, 15), self.width, self, self.mapSize)

        self.frontBase = [(15 * self.width, 15 * self.width), (15 * self.width, 16 * self.width)]
        self.endBase = [(16 * self.width, 15 * self.width), (16 * self.width, 16 * self.width)]

        self.eaten = False
        self.alive = True

        self.vel = 4
        self.current = 0

    def getPosIndex(self, cell):
        for x, part in enumerate(self.pos):
            if cell == part:
                return x

    def snakeCollision(self):
        if self.nextCell in self.pos:
            if len(self.pos) == 1:
                self.alive = False
            else:
                cut = self.getPosIndex(self.nextCell)
                self.pos = self.pos[:cut]
                self.comps = self.comps[:cut +1]

    def move(self, win, r):
        if r < 4:
            if self.compass[r] != self.lastcomp:
                self.lastcomp = self.compass[r]
                # self.setNextCell()
                # self.setFrontBase()
        if self.alive:
            if self.current < self.width:
                self.current += self.vel

                if self.current >= self.width:
                    self.current = self.width

                self.fillFront(win)
                self.fillEnd(win)

            else:
                pygame.draw.rect(win, (0, 255, 0),
                                 (self.pos[-1][0] * self.width, self.pos[-1][1] * self.width, self.width, self.width))
                self.current = 0

                self.pos.insert(0, self.nextCell)
                self.comps.insert(0, self.lastcomp)
                self.setNextCell()

                if not self.eaten:
                    self.endCell = self.pos.pop(-1)
                    self.comps.pop(-1)
                else:
                    self.eaten = False

                self.setFrontBase()
                self.setEndBase()

        for part in self.pos:
            pygame.draw.rect(win, (0, 255, 0), (part[0] * self.width, part[1] * self.width, self.width, self.width))
        self.apple.draw(win)

        self.appleEaten()
        self.snakeCollision()
        self.wallCollision()

    def fillEnd(self, win):
        if self.comps[-1][0] != 0:
            w = (self.width - self.current) * -self.comps[-1][0]
            h = self.width
        else:
            w = self.width
            h = (self.width - self.current) * -self.comps[-1][1]

        if self.comps[-1] != (0, -1):
            pygame.draw.rect(win, (0, 255, 0), (self.endBase[0][0], self.endBase[0][1], w, h))
        else:
            pygame.draw.rect(win, (0, 255, 0), (self.endBase[1][0], self.endBase[1][1], w, h))

    def setEndBase(self):
        oC = ((self.endCell[0] * self.width, self.endCell[1] * self.width),
              ((self.endCell[0] + 1) * self.width, self.endCell[1] * self.width),
              ((self.endCell[0] + 1) * self.width, (self.endCell[1] + 1) * self.width),
              (self.endCell[0] * self.width, (self.endCell[1] + 1) * self.width),
              )
        nC = ((self.pos[-1][0] * self.width, self.pos[-1][1] * self.width),
              ((self.pos[-1][0] + 1) * self.width, self.pos[-1][1] * self.width),
              ((self.pos[-1][0] + 1) * self.width, (self.pos[-1][1] + 1) * self.width),
              (self.pos[-1][0] * self.width, (self.pos[-1][1] + 1) * self.width),
              )

        self.endBase = self.getBase(nC, oC)

    def setFrontBase(self):
        oC = ((self.nextCell[0] * self.width, self.nextCell[1] * self.width),
              ((self.nextCell[0] + 1) * self.width, self.nextCell[1] * self.width),
              ((self.nextCell[0] + 1) * self.width, (self.nextCell[1] + 1) * self.width),
              (self.nextCell[0] * self.width, (self.nextCell[1] + 1) * self.width),
              )
        nC = ((self.pos[0][0] * self.width, self.pos[0][1] * self.width),
              ((self.pos[0][0] + 1) * self.width, self.pos[0][1] * self.width),
              ((self.pos[0][0] + 1) * self.width, (self.pos[0][1] + 1) * self.width),
              (self.pos[0][0] * self.width, (self.pos[0][1] + 1) * self.width),
              )

        self.frontBase = self.getBase(nC, oC)

    def fillFront(self, win):

        if self.lastcomp[0] != 0:
            w = self.current * self.lastcomp[0]
            h = self.width
        else:
            w = self.width
            h = self.current * self.lastcomp[1]

        if self.lastcomp != (0, 1):
            pygame.draw.rect(win, (0, 255, 0), (self.frontBase[0][0], self.frontBase[0][1], w, h))
        else:
            pygame.draw.rect(win, (0, 255, 0), (self.frontBase[1][0], self.frontBase[1][1], w, h))

    def getBase(self, nc, oc):
        end = []
        for part in nc:
            if part in oc:
                end.append(part)
        return end

    def setNextCell(self):
        self.nextCell = (self.pos[0][0] + self.lastcomp[0], self.pos[0][1] + self.lastcomp[1])

    def appleEaten(self):
        if self.nextCell == self.apple.pos:
            self.eaten = True
            self.apple.eaten()

    def wallCollision(self):
        if not -1 < self.nextCell[0] < self.mapSize[0] or not -1 < self.nextCell[1] < self.mapSize[1]:
            self.alive = False


