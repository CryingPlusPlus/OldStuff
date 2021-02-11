from gturtle import *
Karl = Turtle()
Karl.speed(-1)
Karl.hideTurtle()
def kurve(i): 
    for k in range(int((i/3))): 
        Karl.forward(2)
        Karl.right(3)
for i in range (12):
    Karl.startPath()        
    kurve(90)
    Karl.right(90)
    kurve(90)
    Karl.fillPath()
    Karl.right(120)
