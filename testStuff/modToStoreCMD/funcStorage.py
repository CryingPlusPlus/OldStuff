# nimmt commands schreibt sie in ein .py file und importiert die funktion dann mit indexen als marker
# usage: fS = funcStorage(cmds #if you want) 
#maybe fS.store(func) or fS.storeMults([func1, func2]) wenn alle gespeichert sind 
# wenn alle gespeichert sind -> fS.initStorage() und dann mit fS.aFunc(index) die funcs abrufen
# auf info kann man über fS.n_funcs und fS.storedFuncs zugreifen
import os


class funcStorage:
    def __init__(self, cmds=None, imports='import os\n'):
        self.storage = imports + 'def func(index):\n    ' # designed tatsächliche funktion
        self.storedFuncs = '' # speichert info über fuktionen
        self.n_funcs = 0 # speichert anzahl der Funktionen
        self.aFunc = None # schaut ob bereits initialisert wurde und gibt danach funktionen zurück
        self.imported = False #schaut ob bereits initialisiert wurde
        if cmds is not None: #falls bei __init__() schon cmds mitgegeben werden können die hier gespeichert werden
            self.storeMults(cmds)

    def store(self, cmd): #added 1 funktion zu storage gibt den ticker 1 hoch und speichert welche funktion
        if not self.imported:
            self.storedFuncs += cmd + '\n'
            funcAdd = 'if index == ' + str(self.n_funcs) + ':\n        ' + cmd + '\n        return\n    '
            self.storage += funcAdd
            self.n_funcs += 1

    def storeMults(self, cmds): #added X funktionen zu storage gibt den ticker X hoch und speichert welche Funktionen
        if not self.imported:
            for cmd in cmds:
                self.storedFuncs += cmd + '\n'
                funcAdd = 'if index == ' + str(self.n_funcs) + ':\n        ' + cmd + '\n        return\n    '
                self.storage += funcAdd
                self.n_funcs += 1

    def getInfo(self): #returned info
        print('Ticker =', self.n_funcs, '\nFuncs =', self.storedFuncs)

    def initStorage(self): #initialisiert mit import Func die gleichung
        if self.aFunc is None:
            with open('temp.py', 'w') as temp: #schreibt ins file
                temp.write(self.storage)

            self.importFunc() # imported aus dem file
            os.system('del temp.py') # löscht das file
    
    def importFunc(self):
        import temp
        self.aFunc = lambda i : temp.func(i) #assigned aFunc die importierten functionen
        self.imported = True

    def die(self): #eigentlich nur zum spaß hier
        del self
