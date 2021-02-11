# input data
P1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
P1_Bounce = ['9:00', '20:00']

P2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
P2_Bounce = ['10:00', '18:30']

P3 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '16:00']]
P3_Bounce = ['10:00', '20:00']

timeNeeded = 30

#alle lambdas

# smash = lambda callenders, bounce : [[[bounce[i][0], bounce[i][0]]] + callenders[i] + [[bounce[i][1], bounce[i][1]]] for i in range(len(callenders))]

# turnIntoMin = lambda callenders : [[[int(el[0].replace(':', '')), int(el[1].replace(':', ''))] for el in cal] for cal in callenders]

# free = lambda callenders : [[[cal[i-1][-1], cal[i][0]] for i in range(1, len(cal))] for cal in callenders]

# compare = lambda callenders : [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[1] for el1 in callenders[0]]

# reccompare = lambda callenders, newCallenders : reccompare(callenders[1:], newCallenders + [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[0] for el1 in newCallenders]) if len(callenders) > 1 else newCallenders + [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[0] for el1 in newCallenders]

# cut = lambda callenders, timeNeeded : [el for el in callenders if el[1] - el[0] >= timeNeeded]

# turnIntoStr = lambda callenders : [[str(el[0]) if len(str(el[0])) > 3 else '0' + str(el[0]), str(el[1]) if len(str(el[1])) > 3 else '0' + str(el[1])] for el in callenders]

# remDoubles = lambda callenders : [el for i, el in enumerate(callenders) if el not in callenders[:i]]

# turnIntoTime = lambda callenders : [[el[0][:2] + ':' + el[0][2:4], el[1][:2] + ':' + el[1][2:4]] for el in callenders]

#alle verbinden:
# callenders = smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce])
# callenders = turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce]))
# callenders = free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce])))
# callenders = reccompare(free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce])))[2:], compare(free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce])))))
# callenders = cut(reccompare(free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce])))[2:], compare(free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce]))))), timeNeeded)
# callenders = turnIntoStr(cut(reccompare(free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce])))[2:], compare(free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce]))))), timeNeeded))
# callenders = remDoubles(turnIntoStr(cut(reccompare(free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce])))[2:], compare(free(turnIntoMin(smash([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce]))))), timeNeeded)))
callenders = (lambda callenders : [[el[0][:2] + ':' + el[0][2:4], el[1][:2] + ':' + el[1][2:4]] for el in callenders])((lambda callenders : [el for i, el in enumerate(callenders) if el not in callenders[:i]])((lambda callenders : [[str(el[0]) if len(str(el[0])) > 3 else '0' + str(el[0]), str(el[1]) if len(str(el[1])) > 3 else '0' + str(el[1])] for el in callenders])((lambda callenders, timeNeeded : [el for el in callenders if el[1] - el[0] >= timeNeeded])((lambda callenders, newCallenders : reccompare(callenders[1:], newCallenders + [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[0] for el1 in newCallenders]) if len(callenders) > 1 else newCallenders + [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[0] for el1 in newCallenders])((lambda callenders : [[[cal[i-1][-1], cal[i][0]] for i in range(1, len(cal))] for cal in callenders])((lambda callenders : [[[int(el[0].replace(':', '')), int(el[1].replace(':', ''))] for el in cal] for cal in callenders])((lambda callenders, bounce : [[[bounce[i][0], bounce[i][0]]] + callenders[i] + [[bounce[i][1], bounce[i][1]]] for i in range(len(callenders))])([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce])))[2:], (lambda callenders : [[el1[0] if (el1[0] > el2[0]) else el2[0], el1[1] if (el1[1] < el2[1]) else el2[1]] for el2 in callenders[1] for el1 in callenders[0]])((lambda callenders : [[[cal[i-1][-1], cal[i][0]] for i in range(1, len(cal))] for cal in callenders])((lambda callenders : [[[int(el[0].replace(':', '')), int(el[1].replace(':', ''))] for el in cal] for cal in callenders])((lambda callenders, bounce : [[[bounce[i][0], bounce[i][0]]] + callenders[i] + [[bounce[i][1], bounce[i][1]]] for i in range(len(callenders))])([P1, P2, P3], [P1_Bounce, P2_Bounce, P3_Bounce]))))), timeNeeded))))
print(callenders)
