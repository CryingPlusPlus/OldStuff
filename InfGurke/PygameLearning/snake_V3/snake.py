import pygame


class Snake:
    def __init__(self, pos, mapSize, w):
        self.pos = [pos]

        self.mapSize = mapSize
        self.width = w

        self.alive = True
        self.vel = 1

        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.lastComp = self.compass[3]
        self.new_last_comp = self.lastComp

        self.nextCell = (self.pos[0][0] + self.lastComp[0], self.pos[0][1] + self.lastComp[1])
        self.cConec = 0

        self.comps = [self.lastComp]
        self.lastCell = (16, 15)

        self.eaten = False

    def getBase(self):
        nC = ((self.nextCell[0] * self.width, self.nextCell[1] * self.width),
              ((self.nextCell[0] + 1) * self.width, self.nextCell[1] * self.width),
              ((self.nextCell[0] + 1) * self.width, (self.nextCell[1] + 1) * self.width),
              (self.nextCell[0] * self.width, (self.nextCell[1] + 1) * self.width))
        oC = ((self.pos[0][0] * self.width, self.pos[0][1] * self.width),
              ((self.pos[0][0] + 1) * self.width, self.pos[0][1] * self.width),
              ((self.pos[0][0] + 1) * self.width, (self.pos[0][1] + 1) * self.width),
              (self.pos[0][0] * self.width, (self.pos[0][1] + 1) * self.width))
        end = []

        for part in nC:
            if part in oC:
                end.append(part)
        return end

    def apple_collision(self, apple, nextcell):
        if apple.pos == nextcell:
            self.eaten = True
            apple.eaten()

    def getEnd(self):
        nC = ((self.lastCell[0] * self.width, self.lastCell[1] * self.width),
              ((self.lastCell[0] + 1) * self.width, self.lastCell[1] * self.width),
              ((self.lastCell[0] + 1) * self.width, (self.lastCell[1] + 1) * self.width),
              (self.lastCell[0] * self.width, (self.lastCell[1] + 1) * self.width))
        oC = ((self.pos[-1][0] * self.width, self.pos[-1][1] * self.width),
              ((self.pos[-1][0] + 1) * self.width, self.pos[-1][1] * self.width),
              ((self.pos[-1][0] + 1) * self.width, (self.pos[-1][1] + 1) * self.width),
              (self.pos[-1][0] * self.width, (self.pos[-1][1] + 1) * self.width))
        end = []

        for part in nC:
            if part in oC:
                end.append(part)
        end = [(end[0][0] + self.width * self.lastComp[0], end[0][1] + self.width * self.lastComp[1]),
               (end[1][0] + self.width * self.lastComp[0], end[1][1] + self.width * self.lastComp[1])]

        return end

    def getWH(self):
        if self.lastComp[0] != 0:
            w = self.cConec * self.lastComp[0]
        else:
            w = self.width
        if self.lastComp[1] != 0:
            h = self.cConec * self.lastComp[1]
        else:
            h = self.width
        return w, h

    def wallCollision(self):
        if not -1 < self.nextCell[0] < self.mapSize[0] or not -1 < self.nextCell[1] < self.mapSize[1]:
            self.alive = False

    def move(self, win, apple, r=4):
        if r == 4:
            pass
        else:
            self.lastComp = self.compass[r]
            print(r)

        self.apple_collision(apple, self.nextCell)
        self.wallCollision()

        if self.alive:
            # front moving
            if self.cConec < self.width:
                self.cConec += self.vel
                if self.cConec >= self.width:
                    self.cConec = self.width
            else:
                self.cConec = 0
                self.pos.insert(0, self.nextCell)
                # self.lastCell = self.pos.pop(-1)
                self.nextCell = (self.pos[0][0] + self.lastComp[0], self.pos[0][1] + self.lastComp[1])
                self.comps.insert(0, self.lastComp)
                #self.lastComp = self.new_last_comp

                if not self.eaten:
                    self.lastCell = self.pos.pop(-1)
                    self.comps.pop(-1)  # könnte auch oben sein macht aber mehr sinn hier?
                else:
                    self.eaten = False

            base = self.getBase()
            w, h = self.getWH()
            pygame.draw.rect(win, (0, 255, 0), (base[0][0], base[0][1], w, h))

            for x in range(len(self.pos) - 1):
                part = self.pos[0]
                pygame.draw.rect(win, (0, 255, 0), (part[0] * self.width, part[1] * self.width, self.width, self.width))
            end = self.getEnd()

            if self.comps[-1][0] != 0:
                w = w * self.comps[-1][0]
                w = self.width - w
            if self.comps[-1][1] != 0:
                h = h * self.comps[-1][0]
                h = self.width - h
            pygame.draw.rect(win, (0, 255, 0), (end[0][0], end[0][1], w, h))

    def draw(self, win):
        pass
