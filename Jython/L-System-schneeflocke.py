from Lib.myTurtle import *

#erstellt eine zertrierte Ausgabe des Turtle PLaygrounds
tool = myTurtle(800)
tool.drawBorder()

#default Turtle
penWidth(2)
x,y = 0,-200
#svg plotten
Pkt= tool.initPktArray(x,y)

#L-Syteme
debug=False
l=50
alpha=60
code= "F++F++F"

regel= ["F", "F-F++F-F"]
#Ausgabe nach SVG ===============================
fh = tool.open_file("Schneeflocke.svg")
tool.write_file_path(fh, Pkt)
tool.close_file(fh)