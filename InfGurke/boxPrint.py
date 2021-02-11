def printabox(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('nur Chars pls')
    if width <= 2:
        raise Exception('Width muss größer 2 sein')
    if height <= 2:
        raise Exception('Height muss größer als 2 sein')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

try:
    printabox('a', 2, 10)
except Exception as err:
    print('Your Exception: ' + str(err))