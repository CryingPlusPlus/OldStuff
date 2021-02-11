# limit ca 30 000 000 000 000 000
import random

print('Welches Limit wollen sie haben?')
limit = int(input())
zahl = random.randint(0, limit + 1)



def pruefer(n):
    if n < zahl:
        return -1

    if n > zahl:
        return 1

    if n == zahl:
        return 0


def drunter(n, ver):
    pos = pruefer(n)
    if pos == 1:
        return drunter(int(n / 2), ver + 1)
    else:
        if pos + n/2 == -1:
            return [int(n + n/2), ver]
        else:
            return [int(n), ver]

def potenz(x, pot):
    if x / pot >= 10:
        return potenz(x, pot * 10)
    if x / pot < 1:
        return pot / 10
    if x / pot < 10:
        return pot


def naeherung(n, pot, ver):
    if pruefer(n + pot) == -1:
        if pruefer(n + 3 * pot) == -1:
            return naeherung(n + 3 * pot, pot, ver + 1)
        if pruefer(n + 2 * pot) == -1:
            return naeherung(n + 2 * pot, pot, ver + 1)
        else:
            return naeherung(n + pot, pot, ver + 1)

    if pruefer(n + 5 * pot) == 1:

        if pruefer(n + 1 * pot) == 1:
            return naeherung(n, pot / 10, ver + 1)
        if pruefer(n + 2 * pot) == 1:
            return naeherung(n + pot, pot / 10, ver + 1)
        if pruefer(n + 3 * pot) == 1:
            return naeherung(n + 2 * pot, pot / 10, ver + 1)
        if pruefer(n + 4 * pot) == 1:
            return naeherung(n + 2 * pot, pot / 10, ver + 1)

    if pruefer(n) == 0:
        return [int(n), ver]


arr = naeherung(drunter(limit, 0)[0], potenz(drunter(limit, 0)[0], 10), drunter(limit, 0)[1])
print('Zahl: ' + str(zahl) + '\nGuess: ' + str(arr[0]) + '\nVersuche: ' + str(arr[1]))