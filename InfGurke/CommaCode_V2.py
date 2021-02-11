def CommaCode(alist):
    try:
        end = ', '.join(alist[:-1])
        return end + ' and ' + alist[-1]
    except:
        print('Fehler')


spam = ['a', 'b', 'c', 'd']

print(CommaCode(spam))
