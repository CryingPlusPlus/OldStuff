from gturtle import *
Karl = Turtle()
Karl.hideTurtle()
Karl = Turtle()
Karl.setColor("darkgreen")
Karl.setPenColor("green")
Karl.speed(-1)
Karl.hideTurtle()
Karl.setPos(0, 0)

def schnecke(i, l):
    if i <2: 
        repeat 2:
            Karl.forward(l)
            Karl.right(90)
    else: 
        repeat 4: 
            Karl.forward(l)
            Karl.right(90)
        Karl.left(10)
        schnecke(i-1, l*0.9)
schnecke(100, 250)