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
    end = {}

    for key, val in template.items():
        for v in val:
            if v[1] == 'other bag':
                end[key] = 0
    
    for key, _ in end.items():
        if key in template:
            template.pop(key)

    return end, template

def all_in(val, direct):
    for v in val:
        if v[1] not in direct:
            return False

    return True

def who_indirect(direct, template):
    popper = []
    for key, val in template.items():
        if all_in(val, direct):
            end_wert = 0
            for v in val:
                end_wert += v[0] + v[0] * direct[v[1]] 
            direct[key] = end_wert
            popper.append(key)
    
    for key in popper:
        if key in template:
            template.pop(key)
    
    return direct, template

def looper(direct, template):
    if len(template) == 0:
        return direct, template

    direct, template = who_indirect(direct, template)
    return looper(direct, template)

with open('data.txt', 'r') as fh:
    template, _ = rules(fh)
    direct, template = who_direct(template)
    direct, template = looper(direct, template)
    print(direct['shiny gold bag'])
