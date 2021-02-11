import pyperclip as pc

text = pc.paste()
change = []
changewords = ['VERB', 'NOUN', 'ADJECTIVE']

for word in changewords:
    if word in text:
        text = text.split(word)
        a = len(text) - 1
        for i in range(a):
            print('You want to change the ' + str(a) + ' ' + word + ' to?')
            wech = input()
            text[0] += wech + text[1]
            del(text[1])
        if len(text) == 1:
            text = str(text[0])

print(text)
