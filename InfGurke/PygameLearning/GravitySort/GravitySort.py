import pygame
import random

objects = []
for i in range(100):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    objects.append([(x, y), [random.randint(0, 900), 0 - y]])


def drawPoints(win):
    for ob in objects:
        pygame.draw.rect(win, (255, 0, 0), (ob[1][0], ob[1][1], ob[0][0], ob[0][1]))


sorted = []


def moveObj(t):
    for ob in objects:
        force = ob[0][0] * ob[0][1] * t
        ob[1][1] += force
        if ob[1][1] > 600:
            obCop = ob.copy()
            sorted.append(obCop)
            objects.remove(ob)

def endSort():
    end = []
    for ob in sorted:
        end.append(ob[0][0] * ob[0][1])
    print(end)

def main():
    pygame.init()
    win = pygame.display.set_mode((900, 600))
    clock = pygame.time.Clock()
    t = 1
    while True:
        t += 0
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        win.fill((51, 51, 51))
        drawPoints(win)
        moveObj(t)
        if len(objects) <= 0:
            endSort()
        pygame.display.flip()


if __name__ == '__main__':
    main()
