import pygame
import random
from Maze import *
from pygame.locals import *
from Feld import feld
#from farbenListe import farben

width = 600
height = 600
breite = 30
hoehe = 30
seite = 20


def main():
    # setup
    pygame.init()
    gc.enable()
    screen = pygame.display.set_mode((width ,height))
    pygame.display.set_caption('Maze')
    pygame.mouse.set_visible(1)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    mazeLayer = pygame.Surface(screen.get_size())
    mazeLayer = mazeLayer.convert_alpha()
    clock = pygame.time.Clock()

    screen.blit(background, (0, 0))
    pygame.display.flip()

    Maze = maze(mazeLayer, breite, hoehe, seite)
    # Maze.mainGang()
    # Maze.mainGang()
    # Maze.recursiveBackTracking(random.randint(1, breite - 2), random.randint(1, hoehe - 2))
    # Maze.resetCells()
    Maze.update()
    # print('hah')
    # print(Maze.getNeighbor_Hydra([3,3]))
    # draw
    Maze.connectSomethings()
    while Maze.mode == 'idle':
        Maze.recursiveBackTrackingV2()
    Maze.fillUp()
    while Maze.mode == 'solve':
       Maze.solverV2()
    while Maze.mode =='donedone':
        Maze.viewSolution()
        print('sol')
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
        print('\n')
        screen.blit(background, (0, 0))
        Maze.solverV2()
        Maze.recursiveBackTrackingV2()
        Maze.viewSolution()
        Maze.update()
        Maze.show(screen)
        pygame.display.flip()


if __name__ == '__main__': main()
