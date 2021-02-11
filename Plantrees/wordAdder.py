import pickle

with open('words.txt', 'rb') as fh:
    words = pickle.load(fh)

print('gimme - fickdich um zu beenden')
while 1:
    w = input('\n')

    if w == 'fickdich':
        break
    words.append(w)
with open('words.txt', 'wb') as fh:
    pickle.dump(words, fh)

print(words)
