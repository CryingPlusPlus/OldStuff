import random
list = []
for i in range(101):
    if random.randint(0,1) == 1:
        list.append('H')
    else:
        list.append('T')
T_streaks = []
H_streaks = []

current_streak = []
current_el = list[0]

for el in list:
    if el == current_el:
        current_streak.append(el)
    else:
        if current_el == 'H':
            H_streaks.append(current_streak)
            current_el = 'T'
            current_streak = ['T']
        else:
            T_streaks.append(current_streak)
            current_el = 'H'
            current_streak = ['H']

six_Ts = 0
six_Hs = 0
for list in T_streaks:
    if len(list) >= 6:
        six_Ts += 1
for list in H_streaks:
    if len(list) >= 6:
        six_Hs += 1

print('Sechser T: ' + str(six_Ts) + '\nSechser H: ' + str(six_Hs))