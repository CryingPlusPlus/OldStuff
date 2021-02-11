prices = [5, 11, 3, 8, 60, 90]
k = 10

allPoss = lambda buy, sells : [[sell - buy, (buy, sell)] for sell in sells]
remove = lambda cut, tList : [el for el in tList if (cut not in el[1])]

allTrans = []
for i, p in enumerate(prices):
	allTrans += allPoss(p, prices[i+1:])

output = []
history = []
for _ in range(k):
	if len(allTrans) > 0:
		m = max(allTrans, key=lambda x : x[0])
		output.append(m)
		allTrans = remove(m[1][0], allTrans)
		allTrans = remove(m[1][1], allTrans)
		history.append([sum([el[0] for el in output]), *output])

erg = max(history, key=lambda x : x[0])[1:]
print(erg)
