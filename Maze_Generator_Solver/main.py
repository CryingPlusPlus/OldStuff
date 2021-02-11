import pygame, random
from pygame.locals import *
from maze import Maze


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Tig Maze!')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    mazeLayer = pygame.Surface(screen.get_size())
    mazeLayer = mazeLayer.convert_alpha()  # give it some alpha values
    mazeLayer.fill((0, 0, 0, 0))

    newMaze = Maze(mazeLayer)

    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
        newMaze.update()

        screen.blit(background, (0, 0))
        newMaze.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()