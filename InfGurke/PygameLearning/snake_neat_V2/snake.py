import pygame


class Snake:
    def __init__(self, pos, mapSize, w):
        self.mapsize = mapSize
        self.pos = [pos]
        self.alive = True
        self.len = 1
        self.width = w
        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.last_comp = self.compass[3]
        self.vel = 1

        self.new_last_comp = self.last_comp
        self.baseline = None
        self.endline = None

        self.eaten = False

        self.last_comps = []
        self.conec = False
        self.current_conec = 0

        self.current_disconec = self.width

    def getBaseline(self, cell1, cell2):
        end = []
        for p in cell1:
            if p in cell2:
                end.append(p)
        return end

    def apple_collision(self, apple, nextcell):
        if apple.pos == nextcell:
            self.eaten = True
            apple.eaten()

    def connectCells(self, win):
        if self.alive:
            if self.conec:
                self.current_conec += self.vel

                if self.current_conec >= self.width:
                    self.current_conec = self.width
                    self.conec = False

                fx = self.pos[0][0] * self.width
                fy = self.pos[0][1] * self.width
                old_cell = ((fx, fy),
                            (fx + self.width, fy),
                            (fx + self.width, fy + self.width),
                            (fx, fy + self.width))

                nx = fx + (self.new_last_comp[0] * self.width)
                ny = fy + (self.new_last_comp[1] * self.width)
                new_cell = ((nx, ny),
                            (nx + self.width, ny),
                            (nx + self.width, ny + self.width),
                            (nx, ny + self.width))

                self.baseline = self.getBaseline(old_cell, new_cell)

                if self.new_last_comp[0] != 0:
                    w = self.new_last_comp[0] * self.current_conec
                else:
                    w = self.width
                if self.new_last_comp[1] != 0:
                    h = self.new_last_comp[1] * self.current_conec
                else:
                    h = self.width
                pygame.draw.rect(win, (0, 255, 0),
                                 (self.baseline[0][0], self.baseline[0][1], w, h))
                # pygame.draw.polygon(win, (0, 255, 0),
                #                    (self.baseline[0], self.baseline[1], self.endline[0], self.endline[1]))
                if not self.conec:
                    self.current_conec = 0

    def disconnectCells(self, win):
        if self.alive:
            if self.conec:
                self.current_disconec -= self.vel

                if self.current_disconec <= 0:
                    self.current_disconec = 0
                if len(self.last_comps) != 0:
                    if (self.pos[len(self.pos) - 2][0] - self.pos[-1][0], self.pos[len(self.pos) - 2][1] - self.pos[-1][1]) != self.last_comps[-1]:
                        self.last_comps.pop(-1)
                if len(self.last_comps) != 0:
                    lastcomp = self.last_comps[-1]
                else:
                    lastcomp = self.last_comp
                reverseComp = (lastcomp[0] * -1, lastcomp[1] * -1)

                fx = self.pos[-1][0] * self.width
                fy = self.pos[-1][1] * self.width
                old_cell = ((fx, fy),
                            (fx + self.width, fy),
                            (fx + self.width, fy + self.width),
                            (fx, fy + self.width))

                nx = fx + (lastcomp[0] * self.width)
                ny = fy + (lastcomp[1] * self.width)
                new_cell = ((nx, ny),
                            (nx + self.width, ny),
                            (nx + self.width, ny + self.width),
                            (nx, ny + self.width))

                self.endline = self.getBaseline(old_cell, new_cell)
                pygame.draw.line(win, (255, 0, 0), self.endline[0], self.endline[1])

                if reverseComp[0] != 0:
                    w = reverseComp[0] * self.current_disconec
                else:
                    w = self.width
                if reverseComp[1] != 0:
                    h = reverseComp[1] * self.current_disconec
                else:
                    h = self.width
                pygame.draw.rect(win, (0, 255, 0),
                                 (self.endline[0][0], self.endline[0][1], w, h))

                if self.current_disconec <= 0:
                    self.current_disconec = self.width

    def wallCollision(self, newCell):
        if not -1 < newCell[0] < self.mapsize[0] and not -1 < newCell[1] < self.mapsize[1]:
            self.alive = False

    def move(self, apple, r=4):
        if self.alive:
            if r == 4:
                pass
            else:
                self.new_last_comp = self.compass[r]

            if not self.conec:
                self.last_comps.append(self.new_last_comp)
                self.last_comp = self.new_last_comp
                
                newCell = (self.pos[0][0] + self.last_comp[0], self.pos[0][1] + self.last_comp[1])
                self.pos.insert(0, newCell)
                self.wallCollision(newCell)
                self.apple_collision(apple, newCell)
                if self.eaten:
                    self.eaten = False
                else:
                    self.pos.pop(-1)
                self.conec = True
    def draw(self, win):
        if self.alive:
            for i in range(len(self.pos) - 1):
                part = self.pos[i]
                # p1 = (part[0] * self.width, part[1] * self.width)
                # p2 = ((part[0] + 1) * self.width, part[1] * self.width)
                # p3 = ((part[0] + 1) * self.width, (part[1] + 1) * self.width)
                # p4 = (part[0] * self.width, (part[1] + 1) * self.width)
                # pygame.draw.polygon(win, (0, 255, 0), (p1, p2, p3, p4))
                pygame.draw.rect(win, (0, 255, 0), (part[0] * self.width, part[1] * self.width, self.width, self.width))
