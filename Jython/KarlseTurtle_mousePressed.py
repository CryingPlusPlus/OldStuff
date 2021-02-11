from gturtle import *

def onmousePressed(x, y):
    setPos(x, y)
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
makeTurtle(mousePressed=onmousePressed)