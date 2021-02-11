print('Geben sie das ende der Kette ein: ')
end = int(input())
sum = 0
for i in range(1, end):
    sum += 1/i
print(str(sum))