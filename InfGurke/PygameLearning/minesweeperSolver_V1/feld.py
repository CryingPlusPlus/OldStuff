import pygame


class Feld:
    def __init__(self, pos, w, font, m, mr, map):
        self.font = font
        self.pos = pos
        self.width = w
        self.m = m
        self.mr = mr
        self.clicked = False
        self.value = 0
        self.mine = False
        self.text = None
        self.textRect = None
        self.map = map
        self.fontColors = (
            (200, 200, 200), (104, 222, 222), (93, 245, 96), (242, 82, 82), (255, 197, 82), (215, 82, 255),
            (82, 255, 232),
            (47, 50, 150), (99, 47, 150))
        self.marked = False

    def setText(self):
        self.text = self.font.render(str(self.value), True, self.fontColors[self.value], (51, 51, 51))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.pos[0] * self.width + self.width / 2, self.pos[1] * self.width + self.width / 2)

    def draw(self, win):

        if self.marked:
            if self.map.alive:
                pygame.draw.rect(win, (47, 140, 150),
                                 (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))
                win.blit(self.m, self.mr)
            else:
                if self.mine:
                    pygame.draw.rect(win, (47, 140, 150),
                                     (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))
                    win.blit(self.m, self.mr)
                else:
                    pygame.draw.rect(win, (112, 0, 11),
                                     (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))

        if self.clicked:
            # if self.value == 0:
            #    pygame.draw.rect(win, (150, 150, 150),
            #                     (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))
            if self.mine:
                pygame.draw.rect(win, (255, 0, 0),
                                 (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))
            else:
                if not self.marked:
                    win.blit(self.text, self.textRect)

        pygame.draw.line(win, (200, 200, 200), (self.pos[0] * self.width, self.pos[1] * self.width + self.width),
                         (self.pos[0] * self.width + self.width, self.pos[1] * self.width + self.width))
        pygame.draw.line(win, (200, 200, 200),
                         (self.pos[0] * self.width + self.width, self.pos[1] * self.width + self.width),
                         (self.pos[0] * self.width + self.width, self.pos[1] * self.width))
