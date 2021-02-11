from gturtle import *

def onmouseMoved(x, y):
    setHeading(towards(x, y))
    forward(10)
    
makeTurtle(mouseMoved=onmouseMoved)
speed(-1)