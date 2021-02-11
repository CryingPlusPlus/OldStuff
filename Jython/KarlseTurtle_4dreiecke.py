from gturtle import *
Karl = Turtle()
Karl.hideTurtle()

def dreieck(i):
    repeat 3: 
        Karl.forward(i)
        Karl.right(60-180)
repeat 4:
    dreieck(100)
    Karl.right(90)