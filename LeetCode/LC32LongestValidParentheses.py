#closed = [')', ')']
closed = []
#iter über string
s = ")(()()()())"
i = 0

def remove(s, i):
    if i == 0:
        s = s[1:]
    else:
        s = s[:i-1][i:]
    return s
    
while True:
#bruch wenn er über ganzen String drüber ist
    if i >= len(s):
        #falls am Ende der Klammer invalide Öffnungen sind
        #-> closed hat noch elemente und pro element muss ein '(' entfernt werden
        #-> vom ende des Strings an um die schöne Form zu erhaten
        if len(closed) > 0:
            j = 0
            s = s[::-1]
            while True:
                if len(closed) == 0:
                    break
                if s[j] == '(':
                    s = remove(s, j)
                    closed.pop(0)
                else:
                    j += 1
            s = s[::-1]
        break
#wenn klammer aufgeht closed.add('))
    if s[i] == '(':
        closed.append(')')
        i += 1
#wenn klammer zu geht closed.remove(')') falls closed noch voll else element aus string cutten
    elif s[i] == ')':
        if len(closed) > 0:
            closed.pop(0)
            i += 1
        else:
            s = remove(s, i)
#output = len(string)
print(len(s))
print(s)