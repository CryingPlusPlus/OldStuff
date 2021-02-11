import pyinputplus as pyip

def collatz(num):
    print(num)
    if num != 1:
        if num % 2 == 0:
            return collatz(num // 2)
        else:
            return collatz(num * 3 + 1)


print('start?')
a = pyip.inputInt(min=1)
try:
    collatz(a)

except:
    print('Fehler, probiere bitte einen Integer')
