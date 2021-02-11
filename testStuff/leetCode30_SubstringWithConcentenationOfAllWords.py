s = 'barfoofoobarthefoobarman'
words = ["bar","foo","the"]

getShablon = lambda words : sum([len(el) for el in words])

def inWords(s, words):
    output = True
    for el in words:
        if el not in s:
            output = False
    return output

checker = lambda s, words, sha=getShablon(words) : [i for i in range(len(s) - sha) if inWords(s[i:i+sha], words)]

if __name__ == '__main__':
    print(checker(s, words))