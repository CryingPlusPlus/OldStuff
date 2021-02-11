
# input data
P1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
P1_Bounce = ['9:00', '20:00']

P2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
P2_Bounce = ['10:00', '18:30']

P3 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '16:00']]
P3_Bounce = ['10:00', '20:00']

pause = 10

timeNeeded = 20
P1.insert(0, [P1_Bounce[0], P1_Bounce[0]])
P1.append([P1_Bounce[1], P1_Bounce[1]])

P2.insert(0, [P2_Bounce[0], P2_Bounce[0]])
P2.append([P2_Bounce[1], P2_Bounce[1]])

P3.insert(0, [P3_Bounce[0], P3_Bounce[0]])
P3.append([P3_Bounce[1], P3_Bounce[1]])

callenders = [P1, P2, P3]

turnIntoMin = lambda callenders : [[[int(el[0].replace(':', '')), int(el[1].replace(':', ''))] for el in cal] for cal in callenders]

callenders = turnIntoMin(callenders)

free = lambda callenders : [[[cal[i-1][-1], cal[i][0]] for i in range(1, len(cal))] for cal in callenders]

callenders = free(callenders)

reccompare = lambda callenders, newCallenders : reccompare(callenders[1:], newCallenders + [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[0] for el1 in newCallenders]) if len(callenders) > 1 else newCallenders + [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[0] for el1 in newCallenders]

compare = lambda callenders : [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[1] for el1 in callenders[0]]

callenders = reccompare(callenders[2:], compare(callenders))

cut = lambda callenders, timeNeeded : [el for el in callenders if el[1] - el[0] >= timeNeeded]


callenders = cut(callenders, timeNeeded)

# def turnToTime(callenders):
    # newList = []
    # for el in callenders:
        # a = [str(el[0]), str(el[1])]
        # if len(a[0]) < 4:
            # '0' + a
        # newList.append([a[0][:2] + ':' + a[0][2:4], a[1][:2] + ':' + a[1][2:4]]
    # print(newList)

turnIntoStr = lambda callenders : [[str(el[0]) if len(str(el[0])) > 3 else '0' + str(el[0]), str(el[1]) if len(str(el[1])) > 3 else '0' + str(el[1])] for el in callenders]
# turnToTime(callenders)


callenders = turnIntoStr(callenders)

remDoubles = lambda callenders : [el for i, el in enumerate(callenders) if el not in callenders[:i]]
callenders = remDoubles(callenders)
print(callenders)
