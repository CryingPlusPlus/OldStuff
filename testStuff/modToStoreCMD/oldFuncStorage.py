#Plan: eine Funktion machen die wie ein 'Array' funktioniert und diese dann aus dem temp file importieren.
# usage: mach Objekt aus funcStorage mit fS.store(stmt) speicherst du statements ab...
# wenn du alle gespeichert hast fS.initStorage() + fS.importFunc() 
# danach kannst du deine statements mit ihrem index auf fS.aFunc(index) abrufen
# und am ende des files bzw nachdem du die funcs nicht mehr brauchst fS.die() bitte bitte

#tldr: schreibt funktionien in eine funktion schreibt diese in ein .py file importtiert sie und löscht das file

#refractor --> weniger funktionen... einfacher gestalten
import os


class funcStorage:
    def __init__(self):
        self.storage = 'def func(index):\n    '
        self.n_funcs = 0
        self.aFunc = None
        self.imported = False

    def store(self, cmd):
        if not self.imported:
            funcAdd = 'if index == ' + str(self.n_funcs) + ':\n        ' + cmd + '\n        return\n    '
            self.storage += funcAdd
            self.n_funcs += 1

    def storeMults(self, cmds):
        if not self.imported:
            for cmd in cmds:
                funcAdd = 'if index == ' + str(self.n_funcs) + ':\n        ' + cmd + '\n        return\n    '
                self.storage += funcAdd
                self.n_funcs += 1

    def showStorage(self):
        print(self.storage)

    def initStorage(self):
        with open('temp.py', 'w') as temp:
            temp.write(self.storage)
    
    def importFunc(self):
        import temp
        self.aFunc = lambda i : temp.func(i)
        self.imported = True

    # def getFunc(self, index):
        # return temp.func(index)

    def die(self):
        os.system('del temp.py')
        del self

# fS = funcStorage() #testing stuff ignorieren
# fS.store('print(\'Hello World\')')
# fS.store('print(\'Hallo Tribus\')')
# fS.storeMults(['print(\'Hello en\')', 'print(\'hallo de\')'])
# fS.initStorage()
# # import temp
# fS.importFunc()
# fS.aFunc(0)
# fS.aFunc(1)
# fS.die()
