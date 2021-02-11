from gpanel import *
makeGPanel(0,20,0,20)

for i in range(20):
    setColor("green")
    line(i, 0, 20, i)
    setColor("red")
    line(0, i, i, 20)
    setColor("blue")
    line(i,0,0,20-i)
    setColor("orange")
    line(20, i, 20-i, 20)