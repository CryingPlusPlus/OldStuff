import shelve, pprint

firstShelf = shelve.open('WorkingWithShelveData')
hunde = ['Ceasar', 'Boo']
firstShelf['hunde'] = hunde

for dog in firstShelf['hunde']:
    print(dog + ' does the wauwau')

print(pprint.pformat(firstShelf['hunde']))
firstShelf.close()
#very interesting