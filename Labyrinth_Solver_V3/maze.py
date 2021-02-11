from feld import Feld
import random


class Maze:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe

        self.feld = []
        for pos_x in range(self.breite):
            reihe = []
            for pos_y in range(self.hoehe):
                reihe.append(Feld(pos_x, pos_y))

            self.feld.append(reihe)

    def mainGang(self, d):
        drehFelder = []

        for i in range(d):
            drehFelder.append(self.feld[random.randint(1, self.breite - 1)][random.randint(1, self.hoehe - 1)])

        def overlay_sort(list):
            def all_se_same(liste):
                n = 0
                for x in liste:
                    if liste[0].pos_x + liste[0].pos_y != x.pos_x + x.pos_y:
                        n += 1
                if n == 0:
                    return True
                else:
                    return False

            end = []

            def sort(list):
                if all_se_same(list):
                    for x in list:
                        end.append(x)
                else:
                    if list.__len__() > 0:
                        big = []
                        smol = []
                        sum = 0
                        for x in list:
                            sum += x.pos_x + x.pos_y

                        mittel = sum / list.__len__()

                        for x in list:
                            if x.pos_x + x.pos_y <= mittel:
                                smol.append(x)
                            else:
                                big.append(x)
                        sort(smol)
                        sort(big)

            return end

        drehFelder_s = overlay_sort(drehFelder)

        for feld in drehFelder_s:
            print(feld.pos_x + feld.pos_y)
