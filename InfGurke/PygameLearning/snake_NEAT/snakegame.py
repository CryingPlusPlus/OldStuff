import pygame
import neat
import random
import os
import sys
from pygame.locals import *


class Apple:
    def __init__(self, x, y, w, winW, winH, snake):
        self.pos = (x, y)
        self.w = w
        self.color = (255, 0, 0)
        self.winWidth = winW
        self.winHeight = winH
        self.snake = snake

    def draw(self, win):
        part = self.pos
        p1 = (part[0] * self.w, part[1] * self.w)
        p2 = ((part[0] + 1) * self.w, part[1] * self.w)
        p3 = ((part[0] + 1) * self.w, (part[1] + 1) * self.w)
        p4 = (part[0] * self.w, (part[1] + 1) * self.w)
        pygame.draw.polygon(win, self.color, (p1, p2, p3, p4))

    def snakeFree(self):
        end = []
        for y in range(self.winHeight):
            for x in range(self.winWidth):
                if (x, y) not in self.snake.pos:
                    end.append((x, y))
        return end

    def eaten(self):
        self.pos = random.choice(self.snakeFree())


class Snake:
    def __init__(self, map_w, map_h, width):
        self.len = 1
        self.mapWidth = map_w
        self.mapHeight = map_h
        self.pos = self.setPos()
        self.w = width
        self.color = (0, 255, 0)
        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.last_comp = self.compass[3]
        self.vel = 4
        self.check_pos = 0
        self.eatapple = False
        self.alive = True
        self.haseaten = False

    def setPos(self):
        end = []
        for i in range(self.len):
            end.append((self.mapWidth // 2 + i, self.mapHeight // 2))
        return end

    def get_l_comp_i(self):
        for x, part in enumerate(self.compass):
            if part == self.last_comp:
                return x

    def wall_collision(self, nextcell):
        if not (-1 < nextcell[0] < self.mapWidth) or not (-1 < nextcell[1] < self.mapHeight):
            self.alive = False

    def snake_collision(self, nextcell):
        if nextcell in self.pos:
            self.alive = False

    def apple_collision(self, apple, nextcell):
        if apple.pos == nextcell:
            self.haseaten = True
            self.eatapple = True
            apple.eaten()

    def move(self, apple, r='f'):
        if self.alive:
            # self.check_pos += self.vel

            if r == 'f':  # and self.check_pos >= self.w:
                # hier braucht kein code stehen wollte nur eine erinnerung haben
                pass
            elif r == 'l':  # and self.check_pos
                self.last_comp = self.compass[self.get_l_comp_i() - 1]
            elif r == 'r':
                nextp = self.get_l_comp_i() + 1
                if nextp == 4:
                    nextp = 0
                self.last_comp = self.compass[nextp]
            next_cell = (self.pos[0][0] + self.last_comp[0], self.pos[0][1] + self.last_comp[1])
            self.wall_collision(next_cell)
            self.snake_collision(next_cell)
            self.apple_collision(apple, next_cell)
            self.pos.insert(0, next_cell)
            if not self.eatapple:
                self.pos.pop(-1)
            else:
                self.eatapple = False
            self.check_pos = 0

    def draw(self, win):
        if self.alive:
            for part in self.pos:
                p1 = (part[0] * self.w, part[1] * self.w)
                p2 = ((part[0] + 1) * self.w, part[1] * self.w)
                p3 = ((part[0] + 1) * self.w, (part[1] + 1) * self.w)
                p4 = (part[0] * self.w, (part[1] + 1) * self.w)
                pygame.draw.polygon(win, self.color, (p1, p2, p3, p4))


def main():
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    snake = Snake(30, 30, 20)
    apple = Apple(10, 15, 20, 30, 30, snake)
    clock = pygame.time.Clock()
    run = True
    r = ''
    keypressed = False
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                keypressed = True
            else:
                r = 'f'
            if event.type == pygame.KEYUP and keypressed:
                keypressed = False
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    r = 'l'
                    print('l')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    r = 'r'
                    print('r')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    r = 'f'
                    print('f')
            else:
                r = 'f'
        win.fill((51, 51, 51))
        apple.draw(win)
        snake.draw(win)
        snake.move(apple=apple, r=r)
        pygame.display.update()

        if r != 't':
            r = 't'
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
