def all_se_same(liste):
    n = 0
    for x in liste:
        if liste[0] != x:
            n += 1
    if n == 0:
        return True
    else:
        return False


def overlay_list_sorter(list):
    end = []

    def list_sorter(list):
        if all_se_same(list):
            for x in list:
                end.append(x)
        else:
            if list.__len__() > 0:
                big = []
                smol = []
                sum = 0
                for x in list:
                    sum += x
                mittel = sum / list.__len__()

                for x in list:
                    if x <= mittel:
                        smol.append(x)
                    else:
                        big.append(x)
                list_sorter(smol)
                list_sorter(big)

    list_sorter(list)
    if end.__len__() == list.__len__():
        return end


fh = open('unsorted.txt', 'r')
unsorted_list_1 = fh.read().split(';')
fh.close()
unsorted_list = []

for x in unsorted_list_1:
    unsorted_list.append(float(x))

fh = open('sorted.txt', 'w')
sorted_list = overlay_list_sorter(unsorted_list)
for element in sorted_list:
    fh.write(str(element))
    fh.write('\n')
fh.close()
print('done')
