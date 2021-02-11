import pygame
import random


def putInGulag(gulag):
    deeperGulag = []
    i = 1
    while True:
        if i >= len(gulag[-1]):
            break
        if gulag[-1][i - 1] > gulag[-1][i]:
            n = gulag[-1].pop(i)
            deeperGulag.append(n)
            i -= 1
        i += 1
    if len(deeperGulag) > 0:
        gulag.append(deeperGulag)
        return ['putInGulag', gulag]
    else:
        return ['putTogether', gulag]


def putTogether(gulag):
    if len(gulag) > 1:
        print(gulag)

        i = 0
        while True:
            if len(gulag[-1]) <= 0:
                gulag.pop(-1)
                break
            if gulag[len(gulag) - 2][i] > gulag[-1][0]:
                gulag[len(gulag) - 2].insert(i, gulag[-1][0])
                gulag[-1].pop(0)
                i -= 1

            i += 1
        return ['putTogether', gulag]

    else:
        return ['done', gulag]


def stalinSort(list):
    list = [list]
    list = putInGulag(list)
    list = putTogether(list)
    return list


def drawPoints(win, list, n):
    level = 50
    w = 900 / n
    for i in range(len(list)):
        for point in list[i]:
            pygame.draw.rect(win, (255,0,0), (int(point * w), int(level * i) + 550, 10, 10))


def main():
    pygame.init()
    win = pygame.display.set_mode((900, 600))
    clock = pygame.time.Clock()

    list = []
    n = 100
    for i in range(n):
        list.append(random.randint(0, n))
    mode = 'putInGulag'
    list = [list]
    while True:
        clock.tick(10)

        win.fill((51, 51, 51))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #clock.tick(10)
        drawPoints(win, list, n)
        if mode == 'putInGulag':
            p = putInGulag(list)
            mode = p[0]
            list = p[1]
        if mode == 'putTogether':
            p = putTogether(list)
            mode = p[0]
            list = p[1]
        if mode == 'done':
            print(list)
        pygame.display.flip()
if __name__ == '__main__':
    main()

# ich verstehe meinen eigenen code nciht haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ich muss english machen gehen 