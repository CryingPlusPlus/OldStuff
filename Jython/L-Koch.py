from gturtle import *
from Lib.myTurtle import *

#Erstellt eine zentrierte Ausgabe mit Rahmen
tool = myTurtle(1920)
tool.drawBorders()
ht()
#default Turtle
setPos(0,0)
penWidth(2)
x,y=0,0
#Ausgabefunktion
def output(msg):
    if debug:
        print msg

#=========== Main Program ===========

debug=True
l = 50
alpha = 60
#svg start
Pkt= tool.initPktArray(x,y)
#Beginn
code = "F++F++F"

#Einzel Regeln
regel = ["F", "F-F++F-F"]
#Alle Regeln
regeln = [regel]

print "Basis: %s" % (code)

#Iteration ==============================================
anzahl = 4
output(code)
for i in range(0,anzahl):
    #arbeite alle Regeln durch
    for item in regeln:
        output(item)
        code = code.replace(item[0], item[1])
        output(code)
        
print "Fertiger Code: %s" % (code)
#Ausgabe ==============================================
for char in code:
    if char=="F":
        forward(l)
        Pkt.append("%s,%s" % (getX(), getY()))
    if char=="+":
        left(alpha)
    if char=="-":
        right(alpha)
    if char=="f":
        pu()
        forward(l)
        pd()
Pkt.append("%s,%s" % (x, y))
#Ausgabe nach SVG ===============================
fh = tool.open_file("Schneeflocke_tiefe_4.svg")
tool.write_file_path(fh, Pkt)
tool.close_file(fh)    