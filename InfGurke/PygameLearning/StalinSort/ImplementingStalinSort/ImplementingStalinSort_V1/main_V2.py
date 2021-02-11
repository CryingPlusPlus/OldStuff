import random
import time

list = [[]]
n = 10
for i in range(n):
    list[0].append(random.randint(0, n))


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


def rebuild(gulag):
    print(gulag)
    if len(gulag) > 1:
        if len(gulag[-1]) <= 0:
            gulag.pop(-1)

        if gulag[len(gulag) - 2][-1] < gulag[-1][0]:
            for el in gulag[-1]:
                gulag[len(gulag) - 2].append(el)
                gulag.pop(-1)
        elif gulag[len(gulag) - 2][0] > gulag[-1][0]:
            pieces = cut(gulag[-1], -1, gulag[len(gulag) - 2][0])
            i = 0
            for el in pieces[0]:
                gulag[len(gulag) - 2].insert(i, el)
                i += 1
            gulag[-1] = pieces[1]
        else:
            i = 0
            while True:
                if i >= len(gulag[len(gulag) - 2]) - 1:
                    break
                pieces = cut(gulag[-1], gulag[len(gulag) - 2][i], gulag[len(gulag) - 2][i + 1])
                if pieces is not None:
                    for el in pieces[0]:
                        gulag[len(gulag) - 2].insert(i+1, el)
                    gulag[-1] = pieces[1]
                    i -= 1
                i += 1
        return rebuild(gulag)
    else:
        return gulag

list = putInGulag(list)
print(rebuild(list))
