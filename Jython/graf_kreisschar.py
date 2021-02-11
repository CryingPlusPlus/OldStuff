from gpanel import *
makeGPanel(0,20,0,20)
move(0,10)
x=0
y=10
for i in range(11):
    circle(i)
    move(x, y)
    x = x+2
