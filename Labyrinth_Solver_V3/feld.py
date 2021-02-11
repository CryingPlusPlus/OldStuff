class Feld:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ways = [False, False, False, False]

    def update(self):
        pass

    def log(self):
        print(self.feld)
