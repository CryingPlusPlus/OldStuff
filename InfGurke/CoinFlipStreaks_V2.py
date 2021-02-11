import random
list = ''
for i in range(121):
    if random.randint(0,1) == 1:
        list += 'H'
    else:
        list += 'T'

six_Hs = False
six_Ts = False

if 'HHHHHH' in list:
    six_Hs = True
if 'TTTTTT' in list:
    six_Ts = True

print('Sechser T: ' + str(six_Ts) + '\nSechser H: ' + str(six_Hs))

