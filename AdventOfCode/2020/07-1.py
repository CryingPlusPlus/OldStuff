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
            if 'shiny gold' in v[1]:
                end[key] = 1
    
    for key, _ in end.items():
        template.pop(key)
    return end, template

def who_indirect(template, direct):
    popper = []
    for key, val in template.items():
        for v in val:
            if v[1] in direct:
                direct[key] = 1
                popper.append(key)

    for key in popper:
        if key in template:
            template.pop(key)
    
    return direct, template


def looper(template, direct, l):
    direct, template = who_indirect(template, direct)

    if len(template) == l:
        return direct, template
    
    return looper(template, direct, len(template))
        


with open('data.txt', 'r') as fh:
    template, string = rules(fh)
    pprint(template)
    print(len(template))
    print('\n')
    direct, template = who_direct(template)
    pprint(direct)
    print(len(template))
    print('\n')

