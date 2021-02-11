class Ship:
    def __init__(self):
        self.degrees = 0
        self.state = 'east'


        self.pos = {
            'north' : 0,
            'south' : 0,
            'east' : 0,
            'west' : 0,
        }
    
    def compute_instruction(self, instruction):
        com = instruction[0]
        param = int(instruction.split(com)[1])

        if com == 'N':
            self.pos['north'] += param
        if com == 'S':
            self.pos['south'] += param
        if com == 'E':
            self.pos['east'] += param
        if com == 'W':
            self.pos['west'] += param
        if com == 'L':
            self.turn(-param)
        if com == 'R':
            self.turn(param)
        if com == 'F':
            self.pos[self.state] += param
    
    def turn(self, deg):
        self.degrees += deg
        self.degrees = self.degrees % 360

        if self.degrees == 0:
            self.state = 'east'
        if self.degrees == 90:
            self.state = 'south'
        if self.degrees == 180:
            self.state = 'west'
        if self.degrees == 270:
            self.state = 'north'
    
    def get_manhatten_distance(self):
        return abs(self.pos['north'] - self.pos['south']) + abs(self.pos['east'] - self.pos['west'])


def reader():
    instructions = []
    with open('data.txt', 'r') as fh:
        for line in fh:
            line = line.split('\n')[0]
            instructions.append(line)
    return instructions

def main():
    ship = Ship()
    instructions = reader()

    for ins in instructions:
        ship.compute_instruction(ins)

    print(ship.pos)
    print(ship.get_manhatten_distance())

if __name__ == "__main__":
    main()
