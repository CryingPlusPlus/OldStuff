text = input().lower()
vokale = ['a', 'e', 'i', 'o', 'u', 'y']


def transform(word):
    if word.isalpha():
        if word[0] in vokale:
            return word + 'yay'
        else:
            toend = ''
            while True:
                if word[0] in vokale:
                    return word + toend + 'yay'
                else:
                    toend += word[0]
                    word = word[1:]
    else:
        return word


text = text.split(' ')

for i in range(len(text)):
    text[i] = transform(text[i])

text = ' '.join(text)
print(text)
