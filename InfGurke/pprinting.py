import pprint

test = [['Hallo', 'World'],
        ['Apfle', 'Apple', 'Birne'],
        ['Pie', 'Kuchen', 'Torte']]

for i in range(len(test)):
    test[i] = ' '.join(test[i])

pprint.pprint(test)