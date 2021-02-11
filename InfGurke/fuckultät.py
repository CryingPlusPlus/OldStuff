def fckult(n):
    if n == 0:
        return 1
    else:
        n = n * fckult(n - 1)
        return n


print('Hallo bitte zahlt die gefuckt werden soll: ')
x = int(input())
print(fckult(x))