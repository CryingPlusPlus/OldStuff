import shelve, pyperclip, pyinputplus as pyip
dataShelf = shelve.open('UpdateableClipboardData')

if pyip.inputYesNo('You want to add or cahnge?') == 'yes':
    while True:
        dataShelfKeys = list(dataShelf.keys())
        name = pyip.inputStr('Inputname?')
        if name in dataShelfKeys:
            if pyip.inputYesNo('You want to override?') == 'yes':
                break
        else:
            break
    dataShelf[name] = pyperclip.paste()
elif pyip.inputYesNo('You want to read some?') == 'yes':
    while True:
        dataShelfKeys = list(dataShelf.keys())
        name = pyip.inputStr('inputname')
        if name in dataShelfKeys:
            print(dataShelf[name])
            pyperclip.copy(' '.join(dataShelf[name]))
            break
        else:
            print('retry')


dataShelf.close()