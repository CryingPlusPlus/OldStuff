from gturtle import *
from Lib.myTurtle import *

tool = myTurtle(1000)
hideTurtle()
setPos(0, 0)

def turtle_it(i, length):
    if i==0:
        forward(length)
    else:
        i-=1
        length = length/5
        turtle_it(i, length )
        left(26)
        turtle_it(i, length )
        right(94)
        turtle_it(i, length )
        right(56)
        turtle_it(i, length)
        left(26)
        turtle_it(i, length)
        turtle_it(i, length )
        left(30)
        turtle_it(i, length )
        right(50)
        turtle_it(i, length )
        right(34)
        turtle_it(i, length)
        left(66)
        turtle_it(i, length)
setPenColor("darkgreen")
turtle_it(5, 100000)