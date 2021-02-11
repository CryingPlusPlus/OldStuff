from gturtle import *
Karl = Turtle()
Karl.hideTurtle()

def Kreisfigur(i): 
    if i <= 10: 
        Karl.rightArc(10, 360)
    else: 
        Karl.rightArc(i, 360)
        Kreisfigur(i-10)
        
Kreisfigur(100)