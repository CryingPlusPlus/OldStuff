from gturtle import *


makeTurtle()
speed(-1)
def turtle_back2(i):
    i=i-5
    setPenColor("green")
    if i>0:
        i=i-10 
        forward(i)
        left(90)
        turtle_back2(i)
def turtle_back(i): 
    penUp()
    forward(5)
    right(90)
    penDown()
    turtle_back2(i)
    
def turtle_it(i): 
    if i<200: 
        forward(i)
        right(90)
        turtle_it(i+10)
    if i==200: 
        turtle_back(i)    
        
def plotten(): 
    turtle_it()


turtle_it(10)