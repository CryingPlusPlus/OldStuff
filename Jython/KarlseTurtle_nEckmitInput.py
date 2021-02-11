#man kann mi Karlbewegt(n) ein nEck erstellen oder mit fastfraktal(n) ein fast frkatal erstellen
from gturtle import *

Karl = Turtle()
Karl.setColor("darkgreen")
Karl.setPenColor("green")
Karl.speed(-1)
Karl.hideTurtle()
Karl.setPos(0, 0)
def Karlq(g, d):
        if g>0: 
            
            Karl.forward(100)   
            Karl.left(360/d)
            
            g=g-1
            Karlq(g, d)
def Karlbewegt(ecken):
    Karlq(ecken, ecken)

ecken = inputInt("wie viele Ecken soll das n_Eck haben alla")
Karlbewegt(ecken)