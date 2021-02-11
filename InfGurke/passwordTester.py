import re

print('Passwort: ')
pwd = input()
eightChars = re.compile(r'[A-Za-z0-9._%$§/\\()?*+,:;#-]{8,}')
upperCase = re.compile(r'[A-Z]+')
lowerCase = re.compile(r'[a-z]+')
digit = re.compile(r'[0-9]+')

eightChars_que = eightChars.search(pwd)
upperCase_que = upperCase.search(pwd)
lowerCase_que = lowerCase.search(pwd)
digit_que = digit.search(pwd)

if eightChars_que is not None and upperCase_que is not None and lowerCase_que is not None and digit_que is not None:
    print('Good Pasword: ' + str(pwd))
else:
    print('nononono')
