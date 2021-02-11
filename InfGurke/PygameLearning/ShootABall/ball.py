import pygame
import time
import random
class Ball:
    def __init__(self, width, mapSize, font):
        self.firstClick = True
        self.pos = (0,0)
        self.width = width
        self.mapSize = mapSize
        self.start = 0
        self.average = None
        self.text = None
        self.textRect = None
        self.font = font

    def draw(self, win):
        self.text = self.font.render(str(self.average), True, (200,200,200), (51, 51, 51))
        self.textRect = self.text.get_rect()
        self.textRect.center = (100, 100)
        if not self.firstClick:
            pygame.draw.rect(win, (255,0,0), (self.pos[0], self.pos[1], self.width, self.width))

    def setPos(self):
        self.pos = (random.randint(0, self.mapSize[0]), random.randint(0, self.mapSize[1]))
        self.start = time.time()

    def click(self):
        if self.firstClick:
            self.setPos()
            self.firstClick = False
        else:
            mousePos = pygame.mouse.get_pos()
            if self.pos[0] <= mousePos[0] <= self.pos[0] + self.width and self.pos[1] <= mousePos[1] <= self.pos[1] + self.width:
                reac = time.time() - self.start
                if self.average is not None:
                    self.average = (self.average + reac)/2
                else:
                    self.average = reac
                print(self.average)
                self.setPos()