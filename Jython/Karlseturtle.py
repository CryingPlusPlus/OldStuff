#man kann mi Karlbewegt(n) ein nEck erstellen oder mit fastfraktal(n) ein fast frkatal erstellen
from gturtle import *

Karl = Turtle()
Karl.setColor("darkgreen")
Karl.setPenColor("green")
Karl.speed(-1)
Karl.setPos(390, 0)
def Karlq(g, d):
        if g>0: 
            playTone(392, 300)
            Karl.forward(100)   
            Karl.left(360/d)
            playTone(523, 300)
            g=g-1
            Karlq(g, d)
def Karlbewegt(ecken):
    Karlq(ecken, ecken)

def fastfraktal(i):
    if i>1: 
        Karlbewegt(i)
        i=i-1
        fastfraktal(i)
    
fastfraktal(5)
