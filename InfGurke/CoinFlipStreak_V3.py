import random

list = ''
for i in range(101):
    if random.randint(0, 1) == 1:
        list += 'H'
    else:
        list += 'T'

six_Ts = len(list.split('TTTTTT')) - 1
six_Hs = len(list.split('HHHHHH')) - 1

print('Sechser H: ' + str(six_Hs) + '\nSechser T: ' + str(six_Ts))
