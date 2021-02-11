from gpanel import *
makeGPanel(-20, 20, -20, 20)

for i in range(-20, 20):
    for k in range(-10, 0): 
        if i<0: 
            setColor("green")
        if i>0: 
            setColor("blue")
        line(0, -20, i, k)