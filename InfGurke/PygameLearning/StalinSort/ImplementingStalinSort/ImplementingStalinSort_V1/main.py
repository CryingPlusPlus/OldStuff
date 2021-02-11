import random
import time

list = []
n = 50
for i in range(n):
    list.append(random.randint(0, n))
gulag = [list]


# for i in range(1, len(gulag[-1])):
#    print(gulag[-1][i - 1], gulag[-1][i])
# print(gulag[-1])


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
        return putInGulag(gulag)
    else:
        return gulag


def cut(list, a, b):
    if list[0] > a:
        return None
    for i, el in enumerate(list):
        if el > b:
            return [list[:i], list[i:]]
    return [list, []]


def putTogether(gulag):
    if len(gulag) > 1:
        print(gulag)
        time.sleep(1)

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
        return putTogether(gulag)

    else:
        return gulag


def stalinSort(list):
    list = [list]
    list = putInGulag(list)
    list = putTogether(list)
    return list


print(stalinSort(list))
