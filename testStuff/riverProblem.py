import random
height = 5
width = 5

#land = [[random.randint(0,1) for _ in range(width)] for _ in range(height)]

land = [
	[1, 1, 0, 0, 0],
	[0, 0, 1, 1, 0],
	[0, 0, 0, 0, 0],
	[1, 1, 0, 0, 0],
	[0, 1, 1, 0, 0]
]

knownOnes = []
rivers = []
compass = ((1,0), (0,-1), (-1, 0), (0, 1))

def checkOne(cord):
	river = []
	if land[cord[0]][cord[1]] == 1 and cord not in knownOnes:
		river.append(cord)
		knownOnes.append(cord)
		for comp in compass:
			y = cord[0] + comp[0]
			x = cord[1] + comp[1]
			if not x < 0 and not x >= width and not y < 0 and not y >= height:
				river += checkOne((y, x))  
	return river

for y, line in enumerate(land):
	for x, _ in enumerate(line):
		riv = checkOne((y, x))
		if len(riv) > 0:
			rivers.append(len(riv))
print(rivers)