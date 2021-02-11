farben = []
r  = 50
g = 1
b = 0
for i in range(125):
    farben.append((r, g, b))
    if r < 255:
        r += 1
    else:
        r = 0
    if g < 255:
        g += 2
    else:
        g = 1
    if b < 255:
        b += 1
    else:
        b = 0