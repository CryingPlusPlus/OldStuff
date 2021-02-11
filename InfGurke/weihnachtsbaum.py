print('hello')
def dreieck(hoehe):
    end = ''
    unterlaenge = 1 + hoehe * 2
    i = 1
    end = ''
    while i < unterlaenge:
       abstand = int((unterlaenge - i)/2)
       end += ' ' * abstand
       end += '*' * i
       end += '\n'
       i += 2
    return end

def schaft(dicke, hoehe, pos):
    if dicke % 2 == 0:
        dicke += 1
    zeile = ' ' * pos + '*' * dicke
    i = 0
    end = ''
    while i < hoehe:
        i += 1
        end += zeile
        end += '\n'
    return end
def weihnachtsbaum(hoehe, dicke):
    end = dreieck(hoehe)
    unterlaenge = 1 + 2 * hoehe
    if dicke % 2 == 0:
        dicke += 1
    end += schaft(dicke, int(hoehe * 0.5), int((unterlaenge - dicke)/2))
    return end

print(weihnachtsbaum(5, 2))
