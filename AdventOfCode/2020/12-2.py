from math import sqrt, pi, sin, cos
from numpy import arctan

def atan2(y, x):
    if x > 0:
        return arctan(y / x)
    if x < 0 and y >= 0:
        return arctan(y / x) + pi
    if x < 0 and y < 0:
        return arctan(y /x) - pi
    if x == 0 and y > 0:
        return pi / 2
    if x == 0 and y < 0:
        return - pi / 2
    
    raise Exception('Something went wrong')

to_rad = lambda deg : deg * pi / 180
to_deg = lambda rad : rad * 180 / pi

class Ship:
    def __init__(self):
        self.pos = {
            'x' : 0,
            'y' : 0
        }   

        self.waypoint = {
            'x' : 10,
            'y' : 1
        }
    
    def turn(self, deg):
        r = sqrt(self.waypoint['x'] ** 2 + self.waypoint['y'] ** 2)
        phi = atan2(self.waypoint['y'], self.waypoint['x'])

        phi += to_rad(deg)

        self.waypoint['x'] = round(r * cos(phi))
        self.waypoint['y'] = round(r * sin(phi))
    
    def move(self, mult):

        for _ in range(mult):
            self.pos['y'] += self.waypoint['y']
            self.pos['x'] += self.waypoint['x']

    def compute_instruction(self, instruction):
        com = instruction[0]
        param = int(instruction.split(com)[1])

        if com == 'R':
            self.turn(-param)
        if com == 'L':
            self.turn(param)
        if com == 'F':
            self.move(param)
        if com == 'N':
            self.waypoint['y'] += param
        if com == 'S':
            self.waypoint['y'] -= param
        if com == 'E':
            self.waypoint['x'] += param
        if com == 'W':
            self.waypoint['x'] -= param
    
    get_manhatten_distance = lambda self : abs(self.pos['x']) + abs(self.pos['y'])

def reader():
    end = []
    with open('data.txt', 'r') as fh:
        for line in fh:
            line = line.split('\n')[0]
            end.append(line)
    return end


def main():
    ship = Ship()
    instructions = reader()

    for ins in instructions:
        ship.compute_instruction(ins)
    
    print(ship.get_manhatten_distance())

if __name__ == "__main__":
    main()