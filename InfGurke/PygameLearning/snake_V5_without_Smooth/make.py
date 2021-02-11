import pygame
import random


class Apple:
    def __init__(self, pos, w, snake, mapSize):
        self.pos = pos
        self.width = w
        self.snake = snake
        self.mapSize = mapSize

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.pos[0] * self.width, self.pos[1] * self.width, self.width, self.width))

    def eaten(self):
        free = []
        for x in range(self.mapSize[0]):
            for y in range(self.mapSize[1]):
                if (x, y) not in self.snake.pos:
                    free.append((x, y))
        self.pos = random.choice(free)


class Snake:
    def __init__(self, pos, w, vel, mapSize):
        self.pos = [(15, 15), (16, 15)]
        self.width = w
        self.vel = vel
        self.current = 0
        self.mapSize = mapSize
        self.apple = Apple((5, 15), self.width, self, mapSize)

        self.compass = ((0, -1), (1, 0), (0, 1), (-1, 0))
        self.lastComp = self.compass[3]
        self.comps = [self.lastComp, self.lastComp]
        self.eaten = False
        self.nextCell = (self.pos[0][0] + self.lastComp[0], self.pos[0][1] + self.lastComp[1])
        self.alive = True
        self.lastCell = (17, 15)
        self.frontBase = self.setBase(self.lastComp, self.nextCell)
        self.endBase = self.setEndBase(self.comps[-1], self.lastCell)

        print(self.frontBase)
        print(self.endBase)

    def wallCollision(self):
        if not -1 < self.nextCell[0] < self.mapSize[0] or not -1 < self.nextCell[1] < self.mapSize[1]:
            self.alive = False

    def snakeCollision(self):
        if self.nextCell in self.pos:
            self.alive = False

    def appleCollision(self):
        if self.nextCell == self.apple.pos:
            self.eaten = True
            self.apple.eaten()

    def getBase(self, nC, oC):
        end = []
        for part in nC:
            if part in oC:
                end.append(part)
        return end

    def setEndBase(self, comp, pos):
        comp = (-comp[0], -comp[1])

        oC = ((pos[0] * self.width, pos[1] * self.width),
              (pos[0] * self.width + self.width, pos[1] * self.width),
              (pos[0] * self.width + self.width, pos[1] * self.width + self.width),
              (pos[0] * self.width, pos[1] * self.width + self.width)
              )
        #pos = (pos[0] + comp[0], pos[1] + comp[1])

        nC = ((self.pos[-1][0] * self.width, self.pos[-1][1] * self.width),
              (self.pos[-1][0] * self.width + self.width, self.pos[-1][1] * self.width),
              (self.pos[-1][0] * self.width + self.width, self.pos[-1][1] * self.width + self.width),
              (self.pos[-1][0] * self.width, self.pos[-1][1] * self.width + self.width)
              )
        return self.getBase(nC, oC)
    def setBase(self, comp, pos):
        comp = (-comp[0], -comp[1])

        oC = ((pos[0] * self.width, pos[1] * self.width),
              (pos[0] * self.width + self.width, pos[1] * self.width),
              (pos[0] * self.width + self.width, pos[1] * self.width + self.width),
              (pos[0] * self.width, pos[1] * self.width + self.width)
              )
        pos = (pos[0] + comp[0], pos[1] + comp[1])

        nC = ((pos[0] * self.width, pos[1] * self.width),
              (pos[0] * self.width + self.width, pos[1] * self.width),
              (pos[0] * self.width + self.width, pos[1] * self.width + self.width),
              (pos[0] * self.width, pos[1] * self.width + self.width)
              )
        return self.getBase(nC, oC)

    def frontfill(self, win):
        base = self.frontBase
        comp = self.lastComp
        fcolor = (0, 255, 0)
        if comp[0] != 0:
            w = self.current * comp[0]
        else:
            w = self.width
        if comp[1] != 0:
            h = self.current * comp[1]
        else:
            h = self.width

        if comp != (0, 1):
            pygame.draw.rect(win, fcolor, (base[0][0], base[0][1], w, h))
        else:
            pygame.draw.rect(win, fcolor, (base[1][0], base[1][1], w, h))

    def endfill(self, win):
        base = self.endBase
        comp = self.comps[-1]
        #comp = (-comp[0], -comp[1])
        fcolor = (51,51,51)
        bcolor = (0, 255, 0)

        if comp[0] != 0:
            w = self.current * comp[0]
        else:
            w = self.width
        if comp[1] != 0:
            h = self.current * comp[1]
        else:
            h = self.width
        if comp != (0, 1):
            pygame.draw.rect(win, bcolor, (base[0][0] + (self.width * comp[0]), base[0][1]  + (self.width * comp[1]), self.width, self.width))
            pygame.draw.rect(win, fcolor, (base[0][0], base[0][1], w, h))
        else:
            pygame.draw.rect(win, bcolor, (base[1][0] + (self.width * comp[0]), base[1][1] + (self.width * comp[1]), self.width, self.width))
            pygame.draw.rect(win, fcolor, (base[1][0], base[1][1], w, h))

    def move(self, win, r):
        if r < 4:
            self.lastComp = self.compass[r]
            # self.nextCell = (self.pos[0][0] + self.lastComp[0], self.pos[0][1] + self.lastComp[1])
        if self.alive:
            if self.current >= self.width:
                self.current = 0
                self.pos.insert(0, self.nextCell)
                self.comps.insert(0, self.lastComp)
                self.nextCell = (self.pos[0][0] + self.lastComp[0], self.pos[0][1] + self.lastComp[1])

                if not self.eaten:
                    self.lastCell = self.pos.pop(-1)
                    self.comps.pop(-1)
                    #self.endBase = self.setEndBase(self.comps[-1], self.lastCell)
                else:
                    self.eaten = False

                self.frontBase = self.setBase(self.lastComp, self.nextCell)

            else:
                self.current += self.vel
                self.frontfill(win)
                #self.endfill(win)  # irgendwie funktioniert end nicht? baseline müsste falsch sein

        for part in self.pos[:-1]:
            pygame.draw.rect(win, (0, 255, 0), (part[0] * self.width, part[1] * self.width, self.width, self.width))
        self.apple.draw(win)
        self.wallCollision()
        self.snakeCollision()
        self.appleCollision()
        #pygame.draw.line(win, (255,0,0), self.endBase[0], self.endBase[1])
        #self.endfill(win)


def main():
    pygame.init()
    win = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    snake = Snake((15, 15), 20, 3, (30, 30))
    run = True

    while run:
        clock.tick(60)
        r = 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                keypressed = False
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    r = 3
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    r = 1
                if event.key == pygame.K_UP or event.key == ord('w'):
                    r = 0
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    r = 2
            else:
                r = 4

        win.fill((51, 51, 51))
        pygame.display.set_caption("{}".format(len(snake.pos)))
        snake.move(win, r=r)
        pygame.display.flip()

        if not snake.alive:
            break
    return main()


if __name__ == '__main__':
    main()
