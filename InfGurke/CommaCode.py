def CommaCode(list):
    end = ''
    try:
        for el in list[:-1]:
            end += el + ', '

        end += 'and ' + list[-1]
        print(end)

    except:
        print('Fehler')


spam = ['a', 'b', 'c']
CommaCode(spam)
