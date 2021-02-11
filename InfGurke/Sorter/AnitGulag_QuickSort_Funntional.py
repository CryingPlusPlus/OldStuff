import random

liste = []
n = 10000

for i in range(n):
    liste.append(random.randint(0, n))


def get_pivot(list):
    flip = list[0]
    for elm in list:
        if flip > elm:
            return elm
        else:
            flip = elm
    return None


def sort(o_list):
    change = False
    society = []
    for u_list in o_list:
        pivot = get_pivot(u_list)

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
        sort(society)
    else:
        end = []
        for list in society:
            for elm in list:
                end.append(elm)

        print(end)

if __name__ == '__main__':
    sort([liste])