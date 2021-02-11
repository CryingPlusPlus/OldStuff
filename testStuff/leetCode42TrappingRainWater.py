from random import randint
import sys

height = [4,2,0,3,2,5]

def getCol(height, mount):
    output = []
    for _ in range(mount):
        if height > 0:
            output.append(1)
            height -= 1
        else:
            output.append(0)
    return output

height = (lambda height, mount : [getCol(el, mount) for el in height])(height, max(height))
width = len(height)
compass = ((-1, 0), (1, 0))

def waterOut(cord):
    for comp in compass:
        x, y = cord
        while True:
            x += comp[0]
            if x < 0 or x >= width or height[x][y] is None:
                return None 
            elif height[x][y] == 1 or height[x][y] == "w":
                break
    return "w"


output = 0
for x, line in enumerate(height):
    for y, val in enumerate(line):
        if val == 0:
            height[x][y] = waterOut((x, y))
            if height[x][y] == "w":
                output += 1

print(output)