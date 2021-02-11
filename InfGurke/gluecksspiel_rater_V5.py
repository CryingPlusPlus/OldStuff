import random

print('Welches Limit wollen sie haben')
limit = int(input())

zahl = random.randint(0, limit + 1)
print('Das ist die Zahl: ' + str(zahl))


def tester(n):
    if n > zahl:
        return 1
    if n < zahl:
        return -1
    if n == zahl:
        return 0


def guess(max, min, ver):
    mittel = int((max + min) / 2)
    pos = tester(mittel)
    if max - 1 == min:
        return [max - 1, ver]
    if pos == 0:
        return [mittel, ver + 1]
    if pos == 1:
        return guess(mittel, min, ver + 1)
    if pos == -1:
        return guess(max, mittel, ver + 1)


print('Das ist die Zahl: ' + str(guess(limit, 0, 0)[0]) + ' \nDas sind die benötigten Versuche: ' + str(guess(limit, 0, 0)[1]))
