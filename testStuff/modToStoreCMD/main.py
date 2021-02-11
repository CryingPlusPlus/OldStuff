import temp
import importlib


def evaCMD(cmd):
    with open('temp.py', 'w') as temp:
        cmd = 'func = lambda : ' + cmd
        temp.write(cmd)
    importlib.reload(temp)
    temp.func()

