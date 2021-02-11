import pygame


class Feld:
    def __init__(self, pos, w):
        self.pos = pos
        self.width = w

        self.currentFill = 0
        self.vel = 1

    def glow(self, win, color):
        pygame.draw.rect(win, color, (self.pos[0], self.pos[1], self.width, self.width))

    def getBase(self, nC, oC):
        end = []
        for part in nC:
            if part in oC:
                end.append(part)
        return end

    def fill(self, win, comp, fcolor, bcolor):
        comp = (comp[0] * -1, comp[1] * -1)
        if self.currentFill < self.width:
            self.currentFill += self.vel

            if self.currentFill >= self.width:
                self.currentFill = self.width

            pygame.draw.rect(win, bcolor, (self.pos[0], self.pos[1], self.width, self.width))

            oC = ((self.pos[0], self.pos[1]),
                  (self.pos[0] + self.width, self.pos[1]),
                  (self.pos[0] + self.width, self.pos[1] + self.width),
                  (self.pos[0], self.pos[1] + self.width)
                  )
            pos = (self.pos[0] + (comp[0] * self.width), self.pos[1] + (self.width * comp[1]))

            nC = ((pos[0], pos[1]),
                  (pos[0] + self.width, pos[1]),
                  (pos[0] + self.width, pos[1] + self.width),
                  (pos[0], pos[1] + self.width)
                  )
            base = self.getBase(nC, oC)

            if comp[0] != 0:
                w = self.currentFill * -comp[0]
            else:
                w = self.width
            if comp[1] != 0:
                h = self.currentFill * -comp[1]
            else:
                h = self.width

            if comp != (0, -1):
                pygame.draw.rect(win, fcolor, (base[0][0], base[0][1], w, h))
            else:
               pygame.draw.rect(win, fcolor, (base[1][0], base[1][1], w, h))
            base = self.getBase(nC, oC)
            return False
        else:
            self.currentFill = 0
            return True
