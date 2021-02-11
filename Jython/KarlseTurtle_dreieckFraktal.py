from gturtle import *
from Lib.myTurtle import *

tool = myTurtle(1000)

setPos(0, 0)
hideTurtle()
def turtle_it(i, length):
    if i==0:
        forward(length)
    else:
        i-=1
        length = length/3
        turtle_it(i, length )
        left(60)
        turtle_it(i, length )
        right(60)
        turtle_it(i, length )
        left(60)
        turtle_it(i, length )
setPenColor("darkgreen")
turtle_it(7, 50000)