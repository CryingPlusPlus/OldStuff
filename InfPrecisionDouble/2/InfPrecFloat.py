
class InfPrecFloat:
    def __init__(self, num):

        self.vorzeichen = num[0] != '-'
        if not self.vorzeichen:
            num = num[1:]

        self.vor_komma = []
        self.nach_komma = []
        vor, nach = num.split('.')
        self.set_vor_komma(vor)
        self.set_nach_komma(nach)

    
    def set_vor_komma(self, vor):
        for c in vor[::-1]:
            self.vor_komma.append(int(c))
    
    def set_nach_komma(self, nach):
        for c in nach:
            self.nach_komma.append(int(c))
    
    def add_vor_komma(self, sinn, vor):
        new_vor = []

        while len(self.vor_komma) < len(vor):
            self.vor_komma.append(0)
        while len(vor) < len(self.vor_komma):
            vor.append(0)
        
        for s_el, o_el in zip(self.vor_komma, vor):
            temp = sinn + s_el + o_el
            sinn = temp // 10
            new_vor.append(temp % 10)
        
        if sinn > 0:
            new_vor.append(sinn)

        return new_vor

    def add_nach_komma(self, nach):
        new_nach = []
        while len(self.nach_komma) < len(nach):
            self.nach_komma.append(0)
        
        while len(nach) < len(self.nach_komma):
            nach.append(0)

        sinn = 0
        for s_el, o_el in zip(self.nach_komma[::-1], nach[::-1]):
            temp = sinn + s_el + o_el
            sinn = temp // 10
            new_nach.append(temp % 10)

        return sinn, new_nach[::-1]



    
    def __add__(self, other):
        if self.vorzeichen and not other.vorzeichen:
            temp = other
            temp.vorzeichen = True
            return self - temp
        sinn, new_nach = self.add_nach_komma(other.nach_komma)
        new_vor = self.add_vor_komma(sinn, other.vor_komma)

        temp = InfPrecFloat('0.0')
        temp.vor_komma = new_vor
        temp.nach_komma = new_nach

        return temp
    
    def __sub__(self, other):
        print('Subtraktion')


    def __str__(self):
        out = '' if self.vorzeichen else '-'
        for el in self.vor_komma[::-1]:
            out += str(el)
        out += '.'
        for el in self.nach_komma:
            out += str(el)
        
        return out



if __name__ == '__main__':
    myVar = InfPrecFloat('3.241')
    myVar += InfPrecFloat('1.9111111111111111111111111111111111111111111111111111111155555')
    print(myVar)
