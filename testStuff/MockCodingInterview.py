# input data
# P1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
# P1_Bounce = ['9:00', '20:00']

# P2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
# P2_Bounce = ['10:00', '18:30']

# timeNeeded = 30

def getMeetingTime(cal1, bounce1, cal2, bounce2, timeNeeded):
    turnToMin = lambda list :[[
                int(el[0].split(':')[0]) * 60 + int(el[0].split(':')[1]),
                int(el[1].split(':')[0]) * 60 + int(el[1].split(':')[1])
                ] for el in list] 

    free = lambda list : [[list[i-1][-1], list[i][0], list[i][0] - list[i-1][-1]] for i in range(1, len(list))]


    cut = lambda list : [el for el in list if el[-1] >= timeNeeded]

    compare = lambda list1, list2 : [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in list2 for el1 in list1]

    finalCut = lambda list : [el for el in list if (el[0] < el[1])]

    TurnToTime = lambda list : [[(str(el//60) if el//60 >= 10 else ('0' + str(el//60))) + ':' + (str(el%60) if el%60 >= 10 else (str(el%60) + '0')) for el in supEl] for supEl in list]


    cal1.insert(0, ['69:69', bounce1[0]])
    cal1.append([P1_Bounce[1], '69:69'])

    cal2.insert(0, ['69:69', bounce2[0]])
    cal2.append([P2_Bounce[1], '69:69'])

    return TurnToTime(finalCut(compare(cut(free(turnToMin(cal1))), cut(free(turnToMin(cal2))))))

# print(getMeetingTime(P1, P1_Bounce, P2, P2_Bounce, timeNeeded))
