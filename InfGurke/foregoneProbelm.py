import pyinputplus as pyip
N = pyip.inputInt()
i = 1
while True:
    a = N- i
    b = i
    if '4' not in str(a) and '4' not in str(b):
        break
    else:
        i += 1

print('a: ' + str(a))
print('b: ' + str(b))