from gturtle import *
makeTurtle()
ht()
def Karlq(g, d):
        if g>0: 
            
            forward(100)   
            left(360/d)
            Karlq(g-1, d)
def abstral(i): 
    repeat 360/i: 
        Karlq(i,i)
        right(360/i)
i=inputInt("lol gimme numma")

def plotten(): 
    abstral(i)

printerPlot(plotten)
    