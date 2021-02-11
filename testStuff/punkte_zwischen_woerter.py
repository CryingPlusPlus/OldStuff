print('Geben sie das erste Wort ein: ')
wort1 = input()
print('Geben sie das zweite Wort ein: ')
wort2 = input()
length = 30 - (len(wort1) + len(wort2))
for i in range(0, length):
    wort1 += '.'
wort1 += wort2
print(wort1)
