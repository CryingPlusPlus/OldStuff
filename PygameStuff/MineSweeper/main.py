from minemap import Map
import pygame
import math


def main():
    pygame.init()
    width = 1350
    height = 720
    fw = 45

    win = pygame.display.set_mode((width, height))

    clock = pygame.time.Clock()
    map = Map((width // fw, height // fw), fw, 0.21, pygame.font.SysFont('comicsansms', 30))
    map.setMines()
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
        pygame.display.flip()
    main()


if __name__ == '__main__':
    main()
