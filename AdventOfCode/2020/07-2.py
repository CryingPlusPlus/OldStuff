import sys
from pprint import pprint

def rules(fh):
    end = {}
    end1 = ""

    for line in fh:
        line = line.split('.\n')[0]
        line = line.replace('bags', 'bag')
        
        key, val = line.split(' contain ')
        end_val = []
        val = val.split(', ')
        for v in val:
            v = v.split(' ')
            num = 0 if v[0] == 'no' else int(v[0])
            v = ' '.join(v[1:])
            end_val.append([num, v])
        end[key] = end_val
        end1 += key + ' '
    
    return end, end1


def who_direct(template):
    end = {'me':1}

    for key, val in template.items():
        for v in val:
            if v[1] == 'other bag':
                end[key] = 1
    
    for key, _ in end.items():
        if key in template:
            template.pop(key)

    return end, template

# def all_in(val, direct):
#     for v in val:
#         if v[1] not in direct:
#             return False

#     return True

def repper(shiny, template, direct):
    end = []
    for el in shiny:
        if el[1] in template:
            for _ in range(el[0]):
                for sub_el in template[el[1]]:
                    end.append(sub_el)
                me = [1, 'me']
                end.append(me)
    return end

def checker(shiny, direct):
    for el in shiny:
        if el[1] in direct:
            return True
    return False

def cache(shiny, direct, val):
    while not checker(shiny, direct):
        for i, el in enumerate(shiny):
            if el[1] in direct:
                val += el[0]
                shiny.pop(i)
                break
    return val, shiny


def looper(shiny, direct, template, val):
    

    while len(shiny) > 0:
        shiny = repper(shiny, template, direct)
        val, shiny = cache(shiny, direct, val)

    return val


with open('data.txt', 'r') as fh:
    template, _ = rules(fh)
    direct, template = who_direct(template)
    shiny = template['shiny gold bag']
    val = looper(shiny, direct, template, 0)
    print(val)