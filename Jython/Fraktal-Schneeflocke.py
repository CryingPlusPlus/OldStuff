from gturtle import *
from lib.myTurtle import *


#Erstellt eine zentrierte Ausgabe mit Rahmen
tool = myTurtle(800)
tool.drawBorders()
#default Turtle
penWidth(2)


def turtle_it(i,length,Pkt):
    if i==0:
        #zeichne Linie
        forward(length)
        
        #neue Position merken
        x_new = getX()
        y_new = getY()
        
        #Pkt Koordinate als "x y"
        Pkt.append("%s,%s" % (x_new, y_new))
    else:
        i = i -1
        length = length/3
        turtle_it(i,length,Pkt)
        left(60)
        turtle_it(i,length,Pkt)
        right(120)
        turtle_it(i,length,Pkt)
        left(60)
        turtle_it(i,length,Pkt)

#=========== Main Program ===========

#am Screen verschieben
x,y = 0,-200
setPos(x,y)

#Punkte Array, move Turtle zu SVG Mitte
Pkt = tool.initPktArray(x,y)
ht()
right(-30)
for x in range(0, 3):
    turtle_it(3, 400, Pkt)
    right(120)


#Ausgabe nach SVG ==================================
fh = tool.open_file("Schneeflocke.svg")
tool.write_file_path(fh, Pkt)
tool.close_file(fh)
