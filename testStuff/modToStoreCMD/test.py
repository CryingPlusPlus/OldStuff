# import os
import temp
import inspect
# import importlib
# import sys
# # func = lambda : print('MoinMoin')



# def evaCMD(cmd):
    # with open('temp.py', 'w') as temp:
        # cmd = 'func = lambda : ' + cmd
        # temp.write(cmd)
    # import temp
    # temp.func()
    # # os.system('del temp.py')
    # # sys.modules.pop('temp')


# # cmds = [
        # # 'print(\'Hello English\')',
        # # 'print(\'Hallo Deutsch\')'
        # # ]

# # for cmd in cmds:
    # # evaCMD(cmd)


# for name, data in inspect.getmembers(temp):
    # if name.startswith('__'):
        # continue
    # print('{} : {!r}'.format(name, data))

for name, data in inspect.getmembers(temp):
    if name.startswith('__'):
        continue
    name
