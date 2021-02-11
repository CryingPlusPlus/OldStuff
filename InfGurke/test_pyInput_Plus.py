import pyinputplus as pyip

age = pyip.inputNum('Ur Age: ')
print('Ur Age is: ' + str(age))

print('\n')

email = pyip.inputEmail('Ur Mail: ', limit=3, default='some@domain.com')
print('UR Mail: ' + email)