import pygame
import random
from Maze import *
from pygame.locals import *
from Feld import feld

width = 500
height = 500
breite = 20
hoehe = 20
seite = 25


def main():
    # setup
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Maze')
    pygame.mouse.set_visible(1)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    mazeLayer = pygame.Surface(screen.get_size())
    mazeLayer = mazeLayer.convert_alpha()
    clock = pygame.time.Clock()

    Feld = feld(mazeLayer, 2,2, 100)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Maze = maze(mazeLayer, breite, hoehe, seite)

    # draw
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        screen.blit(background, (0, 0))
       # feld.update()
        feld.show(screen)
        pygame.display.flip()


if __name__ == '__main__': main()
