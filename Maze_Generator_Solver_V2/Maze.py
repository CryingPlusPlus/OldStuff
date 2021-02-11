import pygame
import random
from Feld import feld
from __main__ import *
import gc


class maze:

    def __init__(self, mazeLayer, breite, hoehe, feldSeite, ):
        self.breite = breite
        # self.farben = farben
        # self.farben_index = 0
        self.hoehe = hoehe
        self.mazeLayer = mazeLayer
        self.state = 'build'
        self.feldSeite = feldSeite
        self.feld = []
        self.totalCells = breite * hoehe
        self.gang = [[random.randint(1, self.breite - 2), random.randint(1, self.hoehe - 2)]]
        self.sol = []
        self.bau = True
        self.hydra = [[[0, 0]]]
        self.solve_bau = True
        self.mode = 'idle'
        self.n_snakes = 1
        self.solution = [[1, 1], [0, 0], [2, 3], [8, 5]]
        for pos_x in range(self.breite):
            felder = []
            for pos_y in range(self.hoehe):
                felder.append(feld(mazeLayer, pos_x, pos_y, self.feldSeite))

            self.feld.append(felder)

    def getNeighbor_Hydra(self, cell):
        richtungen = []
        end = []
        for i in range(4):
            if self.feld[cell[0]][cell[1]].ways[i]:
                richtungen.append(i)
        # print(richtungen)
        for door in richtungen:
            if door == 2:
                if not self.feld[cell[0]][cell[1] + 1].visited:
                    end.append([cell[0], cell[1] + 1])
            if door == 1:
                if not self.feld[cell[0] + 1][cell[1]].visited:
                    end.append([cell[0] + 1, cell[1]])
            if door == 0:
                if not self.feld[cell[0]][cell[1] - 1].visited:
                    end.append([cell[0], cell[1] - 1])
            if door == 3:
                if not self.feld[cell[0] - 1][cell[1]].visited:
                    end.append([cell[0] - 1, cell[1]])

        return end

    def solver(self):
        for i in range(20):
            if self.solve_bau:
                c_Snake = self.hydra[0]
                c_Cell = c_Snake[-1]
                self.feld[c_Cell[0]][c_Cell[1]].visited = True
                self.feld[c_Cell[0]][c_Cell[1]].snake = True
                self.feld[c_Cell[0]][c_Cell[1]].snakeUpdate()

                N_cells = self.getNeighbor_Hydra(c_Cell)

                if N_cells.__len__() > 0:
                    self.hydra[0].append(N_cells[0])
                    if N_cells[0] == [self.breite - 1, self.hoehe - 1]:
                        self.solve_bau = False
                else:
                    noSnake = self.hydra[0].pop()
                    self.feld[noSnake[0]][noSnake[1]].snake = False
                    self.feld[noSnake[0]][noSnake[1]].snakeUpdate()
            else:
                self.feld[self.breite - 1][self.hoehe - 1].snake = True
                self.feld[self.breite - 1][self.hoehe - 1].snakeUpdate()

    def cleanScreen(self):
        for pos_x in range(self.breite):
            for pos_y in range(self.hoehe):
                self.feld[pos_x][pos_y].snake = 0
                self.feld[pos_x][pos_y].snakeUpdate()

    def oneWay(self, cell):
        if not self.feld[cell[0]][cell[1]].visited:
            end = 0
            ways = self.feld[cell[0]][cell[1]].ways

            if ways[0]:
                if not self.feld[cell[0]][cell[1] - 1].visited:
                    end += 1
            if ways[1]:
                if not self.feld[cell[0] + 1][cell[1]].visited:
                    end += 1
            if ways[2]:
                if not self.feld[cell[0]][cell[1] + 1].visited:
                    end += 1
            if ways[3]:
                if not self.feld[cell[0] - 1][cell[1]].visited:
                    end += 1
            if end == 1:
                return True
            else:
                return False
        else:
            return False

    def fillUp(self):
        sackgassen = True
        if self.mode == 'done':
            while sackgassen:
                print('searching')
                gefunden = 0
                for x in range(1, self.breite - 1):
                    for y in range(1, self.hoehe - 1):
                        if not (x == self.breite - 1 and y == self.hoehe - 1) and not (x == 0 and y == 0):
                            if self.oneWay([x, y]):
                                self.feld[x][y].visited = True
                                gefunden += 1
                if gefunden == 0:
                    sackgassen = False
                    self.mode = 'solve'

    def connectSomethings(self):
        for i in range(int(self.breite * self.hoehe * 0.1)):
            print('connecting')
            pos_x = random.randint(2, self.breite - 2)
            pos_y = random.randint(2, self.hoehe - 2)
            richtung = random.randint(0, 3)

            cell_a = [pos_x, pos_y]
            if richtung == 0:
                cell_b = [pos_x, pos_y - 1]
            elif richtung == 1:
                cell_b = [pos_x + 1, pos_y]
            elif richtung == 2:
                cell_b = [pos_x, pos_y + 1]
            else:
                cell_b = [pos_x - 1, pos_y]

            self.connectCells(cell_a, cell_b)

    def viewSolution(self):
        for i in range(100):
            if self.mode == 'donedone':
                if self.solution.__len__() > 0:
                    cell = self.solution[-1]
                    # self.feld[cell[0]][cell[1]].feld_clr = self.farben[self.farben_index]
                    self.feld[cell[0]][cell[1]].snake += 1
                    self.feld[cell[0]][cell[1]].snakeUpdate()
                    self.solution.pop()

                    # if self.farben_index < self.farben.__len__() - 1:
                    #    self.farben_index += 1
                    # else:
                    #    self.farben_index = 0

                else:
                    self.mode = 'donedonedone'

    def solverV2(self):
        if self.mode == 'solve':
            for i in range(1):
                if self.mode == 'solve':
                    print('solving')
                    newSnakess = []
                    deadSnakess = []
                    for snake in self.hydra:
                        c_Cell = snake[-1]
                        self.feld[c_Cell[0]][c_Cell[1]].visited = True
                        self.feld[c_Cell[0]][c_Cell[1]].snake += 1
                        self.feld[c_Cell[0]][c_Cell[1]].snakeUpdate()
                        if c_Cell == [self.breite - 1, self.hoehe - 1]:
                            self.solution = snake
                            self.solution.reverse()
                            self.cleanScreen()
                            self.mode = 'donedone'
                            return
                        Neighbors = self.getNeighbor_Hydra(c_Cell)

                        for cell in Neighbors:
                            newSnake = snake.copy()
                            newSnake.append(cell)
                            newSnakess.append(newSnake)
                        deadSnakess.append(snake)
                    for snake in deadSnakess:
                        self.hydra.remove(snake)
                        # for cell in snake:
                        #    self.feld[cell[0]][cell[1]].snake -= 1
                        #    self.feld[cell[0]][cell[1]].snakeUpdate()
                    for snake in newSnakess:
                        self.hydra.append(snake)
                        # for cell in snake:
                        #    self.feld[cell[0]][cell[1]].snake += 1
                        #    self.feld[cell[0]][cell[1]].snakeUpdate()
            #gc.collect()

    def update(self):

        for pos_x in range(self.breite):
            for pos_y in range(self.hoehe):
                self.feld[pos_x][pos_y].update()

    def show(self, screen):

        for pos_x in range(self.breite):
            for pos_y in range(self.hoehe):
                self.feld[pos_x][pos_y].show(screen)

    def resetCells(self):
        for pos_x in range(self.breite):
            for pos_y in range(self.hoehe):
                self.feld[pos_x][pos_y].visited = False
        self.feld[0][0].visited = True

    def relativePos(self, cell_a, cell_b):

        if cell_a[0] - cell_b[0] == 1:
            return [3, 1]
        if cell_a[0] - cell_b[0] == -1:
            return [1, 3]
        if cell_a[1] - cell_b[1] == 1:
            return [0, 2]
        if cell_a[1] - cell_b[1] == -1:
            return [2, 0]

    def getNeighbor(self, pos_x, pos_y):
        Ns = []
        if pos_x - 1 >= 0:
            if not self.feld[pos_x - 1][pos_y].visited:
                Ns.append([pos_x - 1, pos_y])

        if pos_x + 1 <= self.breite - 1:
            if not self.feld[pos_x + 1][pos_y].visited:
                Ns.append([pos_x + 1, pos_y])

        if pos_y - 1 >= 0:
            if not self.feld[pos_x][pos_y - 1].visited:
                Ns.append([pos_x, pos_y - 1])

        if pos_y + 1 <= self.hoehe - 1:
            if not self.feld[pos_x][pos_y + 1].visited:
                Ns.append([pos_x, pos_y + 1])
        # print(Ns)
        return random.choice(Ns)

    def hasNeighbor(self, pos_x, pos_y):
        n = 0
        if pos_x - 1 >= 0:
            if not self.feld[pos_x - 1][pos_y].visited:
                n += 1
        if pos_x + 1 <= self.breite - 1:
            if not self.feld[pos_x + 1][pos_y].visited:
                n += 1
        if pos_y - 1 >= 0:
            if not self.feld[pos_x][pos_y - 1].visited:
                n += 1
        if pos_y + 1 <= self.hoehe - 1:
            if not self.feld[pos_x][pos_y].visited:
                n += 1

        if n > 0:
            return True
        else:
            return False

    def connectCells(self, cell_a, cell_b):
        richtung = self.relativePos(cell_a, cell_b)

        self.feld[cell_a[0]][cell_a[1]].ways[richtung[0]] = True
        self.feld[cell_b[0]][cell_b[1]].ways[richtung[1]] = True

    def recursiveBackTracking(self, pos_x, pos_y):

        self.feld[pos_x][pos_y].visited = True
        # print(pos_y, pos_x)
        if self.hasNeighbor(pos_x, pos_y):
            self.gang.append([pos_x, pos_y])
            N = self.getNeighbor(pos_x, pos_y)
            self.connectCells([pos_x, pos_y], N)
            self.recursiveBackTracking(N[0], N[1])
        else:
            self.gang.pop()
            if self.gang.__len__() > 0:
                self.recursiveBackTracking(self.gang[-1][0], self.gang[-1][1])
            else:
                pass

    def recursiveBackTrackingV2(self):
        # print('idling')
        if self.mode == 'idle':
            print('idling')
            # for i in range(100):
            if self.mode == 'idle':
                c_Cell = self.gang[-1]
                # if self.gang.__len__() > 1:
                #    b_cell = self.gang[-2]
                #    self.feld[b_cell[0]][b_cell[1]].feld_clr = (255, 255, 255)
                # self.feld[c_Cell[0]][c_Cell[1]].feld_clr = (255, 0, 0)
                self.feld[c_Cell[0]][c_Cell[1]].visited = True

                if self.hasNeighbor(c_Cell[0], c_Cell[1]):
                    n_Cell = self.getNeighbor(c_Cell[0], c_Cell[1])
                    self.gang.append(n_Cell)
                    self.connectCells(c_Cell, n_Cell)
                else:
                    self.gang.pop()
                if self.gang.__len__() == 0:
                    self.mode = 'done'
                    self.connectSomethings()
                    self.resetCells()

    # get cell - get Nepassighborcell go to neighborcell
