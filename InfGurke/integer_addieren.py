print('Wie viele Integer?')
x = int(input())
sum = 0

for i in range(0, x):
    print('integer: ')
    y = int(input())
    sum += y

print('das ist die Summe: ' + str(sum))
