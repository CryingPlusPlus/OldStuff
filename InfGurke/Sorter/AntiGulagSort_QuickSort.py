import random
import time

class Sorter:
    def __init__(self):
        self.end = []

    def get_pivot(self, list):
        flip = list[0]
        for elm in list:
            if flip > elm:
                return elm
            else:
                flip = elm
        return None

    def listmaker(self, n):
        list = []
        for i in range(n):
            list.append(random.randint(0, n))
        return list

    def sort(self, o_list):
        change = False
        society = []
        for u_list in o_list:
            pivot = self.get_pivot(u_list)

            if pivot is not None:
                change = True
                gulag = [[], [], []]

                for elm in u_list:
                    if elm < pivot:
                        gulag[0].append(elm)
                    elif elm == pivot:
                        gulag[1].append(elm)
                    else:
                        gulag[2].append(elm)
                for li in gulag:
                    if li.__len__() > 0:
                        society.append(li)
            else:
                society.append(u_list)

        if change:
            #print(society)
            #print('')
            #time.sleep(1.5)
            self.sort(society)
        else:
            self.end = []
            for list in society:
                for elm in list:
                    self.end.append(elm)

        return self.end



def main(n):
    Stalin = Sorter()
    list = Stalin.listmaker(n)

    print(Stalin.sort([list]))
    # print(Stalin.get_pivot([3, 4, 8, 10, 0, 3, 4, 5, 10]))


if __name__ == '__main__':
    main(1000000)
