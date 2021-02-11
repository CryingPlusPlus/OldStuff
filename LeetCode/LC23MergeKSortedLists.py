from random import randint


#mergeSort
def merge(a, b):
    output = []
    ai = 0
    bi = 0
    lena = len(a)
    lenb = len(b)
    while True:
        if ai >= lena or bi >= lenb:
            break
        if a[ai] < b[bi]:
            output.append(a[ai])
            ai += 1
        else:
            output.append(b[bi])
            bi += 1
    # for el in a[ai:]:
    #     output.append(el)
    # for el in b[bi:]:
    #     output.append(el)
    output += a[ai:] + b[bi:]
    return output

def mergeN(list):
    if list == []:
        return [[]]
    if len(list) < 2:
        return list
    list = [merge(list[0], list[1])] + list[2:]
    return mergeN(list)

if __name__ == '__main__':
    a = [randint(0, 100) for _ in range(10)]
    b = [randint(0, 100) for _ in range(10)]
    c = [randint(0, 100) for _ in range(10)]
    a.sort()
    b.sort()
    c.sort()
    # output = mergeN([a, b, c])
    output = mergeN([[], []])
    print(*output)