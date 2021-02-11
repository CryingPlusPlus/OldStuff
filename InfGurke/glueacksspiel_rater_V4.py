import random

print('Welches Limit wollen sie haben?')
limit = int(input())
zahl = random.randint(0, limit + 1)
print('Zufallszahl: ' + str(zahl))

def game(n):
    if n > zahl:
        return 1
    if n < zahl:
        return -1
    else:
        return 0

def inkrement(deepness):
    if limit / deepness <= 1:
        return 1
    else:
        return int(limit / deepness)

def naeherung(n, deep, ver):
    ink = inkrement(deep)
    if game(n - ink) == 1:
        return naeherung(n - ink, deep + 1, ver + 1)
    if game(n - ink) == -1:
        return naeherung(n, deep + 1, ver + 1)
    if game(n - ink == 0):
        return [n - ink, ver]

print(naeherung(limit, 2, 0))