from gturtle import *


def onClick(x, y):
    Karl.fill(x, y)      
Karl = Turtle(mouseHit = onClick)
Karl.hideTurtle()        
def Karlq(g, d):
        if g>0: 
            
            Karl.forward(100)   
            Karl.left(360/d)
            Karlq(g-1, d)
def abstral(i): 
    repeat 360: 
        Karlq(i,i)
        Karl.right(360/i)
abstral(inputInt("wie viele Ecken soll das n_Eck haben, das wird dann oft genug um sich selbst gedreht damit sich ein kreis ergibt"))