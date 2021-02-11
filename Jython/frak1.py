from gturtle import *
from Lib.myTurtle import *

def open_file(name): 
    return open(name, "w")
def write_file(handle, data): 
    handle.write(data + '\n')
def close_file(handle): 
    return handle.close()
def write_svg_header(handle): 
    write_file(handle, '<?xml version="1.0" encoding="UTF-8"?>')
    write_file(handle,'<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">')
    write_file(handle,'<svg xmlns="http://www.w3.org/2000/svg"')
    write_file(handle,'    xmlns:xlink="http://www.w3.org/1999/xlink"')
    write_file(handle,'    version="1.1" baseProfile="full"')
    write_file(handle,'    width="800mm" height="600mm"')
    write_file(handle,'    <title>Titel der Datei</title>')
    write_file(handle,'    <desc>Beschreibung/Textalternative zum Inhalt.</desc>')
def write_svg_footer(handle):
    write_file(handle,'</svg>')
tool = myTurtle(1000)
hideTurtle()
setPos(300, -500)
def turtle_it(i, length, handle):
    if i==0:
        oldX = round(getX())
        oldY = round(getY())
        forward(length)
        newX = round(getX())
        newY = round(getY())
    else:
        i-=1
        length = length/3
        turtle_it(i, length, handle )
        right(30)
        turtle_it(i, length, handle )
        right(120)
        turtle_it(i, length , handle)
        right(120)
        turtle_it(i, length, handle)
        left(90)
        turtle_it(i, length, handle)
fh = open_file("Fraktal-1.svg")
write_svg_header(fh)
turtle_it(6, 1000, fh)


write_svg_footer(fh)
close_file(fh)