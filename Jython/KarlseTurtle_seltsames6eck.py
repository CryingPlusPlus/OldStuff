from gturtle import *
Karl = Turtle()
Karl = Turtle()
Karl.setColor("darkgreen")
Karl.setPenColor("green")
Karl.speed(-1)
Karl.setPos(0, 0)
def Karlq(g, d):
        if g>0: 
            
            Karl.forward(100)   
            Karl.left(360/d)
            
            g=g-1
            Karlq(g, d)
def Karlbewegt(ecken):
    Karlq(ecken, ecken)
for i in range(24):
    Karlbewegt(6)
    Karl.right(360/15)