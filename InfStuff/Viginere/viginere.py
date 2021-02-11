wort = 'helloworld'
key = 'earth'

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' ']
len = len(a)
quad = [a]

for i in range(1, len):
    quad.append([])

b = []
for j in range(0, len - 1):
    for i in range(1, len):
        quad[j + 1].append(quad[j][i])
    quad[j + 1].append(quad[j][0])


def letter_to_nmb(letter):
    for i in range(0, len):
        if letter == a[i]:
            return i


def str_to_nmb_arr(s):
    s_list = list(s)
    arr = []
    for chars in s_list:
        arr.append(letter_to_nmb(chars))
    return arr


def key_in_length(b_word, b_key):
    end_key = str_to_nmb_arr(b_key)
    word = str_to_nmb_arr(b_word)

    if end_key.__len__() < word.__len__():
        k = end_key
        for i in range(0, (word.__len__() - end_key.__len__())):
            end_key.extend(k)
    while end_key.__len__() > word.__len__():
        end_key.pop()
    return end_key

def convert(s):
       end = ''
       for x in s:
              end += x
       return end

def decode(b_word, b_key):
    word = str_to_nmb_arr(b_word)
    kei = key_in_length(b_word, b_key)
    end = []
    for index in range(0, word.__len__()):
        end.append(quad[kei[index]][word[index]])
    return convert(end)
print(decode('wort ich hasse menschen', 'a'))
