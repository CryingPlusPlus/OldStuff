from minesweeperSolver_V4.map import Map
import pygame
import math
from minesweeperSolver_V4.solver import Solver
import os


def main():
    pygame.init()
    width = 1350
    height = 720
    fw = 45

    win = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    map = Map((width // fw, height // fw), fw, 0.21, pygame.font.SysFont('comicsansms', 30))
    map.setMines()
    solver = Solver(map)
    run = True
    firstClick = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if map.won:
                    run = False
                else:
                    if map.alive:
                        pos = pygame.mouse.get_pos()
                        if firstClick:
                            map.firstClick((math.floor(pos[0] / fw), math.floor(pos[1] / fw)))
                            firstClick = False
                        else:
                            if event.button == 1:
                                # print(pos)
                                # print(math.floor(pos[0] / fw), math.floor(pos[1] / fw))
                                map.feldClicked((math.floor(pos[0] / fw), math.floor(pos[1] / fw)))
                            if event.button == 3:
                                map.feldMarked((math.floor(pos[0] / fw), math.floor(pos[1] / fw)))


                    else:
                        run = False

        win.fill((51, 51, 51))
        map.draw(win)

        if not firstClick and not map.won:
            solver.clicking()
        else:
            firstClick = False
            map.firstClick((10, 10))
        pygame.display.flip()
        if map.won or not map.alive:
            break

    return map.won


def trial(show):
    loss = 0
    win = 0
    width = 1350
    height = 720
    fw = 45
    for i in range(10000):
        if show:
            if main():
                win += 1
            else:
                loss += 1
        else:
            map = Map((width // fw, height // fw), fw, 0.21, None)
            map.setMines()
            solver = Solver(map)
            firstClick = True
            while True:
                if not firstClick and not map.won:
                    solver.clicking()
                else:
                    firstClick = False
                    map.firstClick((10, 10))
                pygame.display.flip()
                if map.won or not map.alive:
                    break
            if map.won:
                win += 1
            else:
                loss += 1
        #os.system('cls')
        print(i)

    print('Winpercentage', win / (loss + win))
    # print('Loss', loss)


if __name__ == '__main__':
    trial(show=True) #show false does not work yet

#linked cells implementieren!
