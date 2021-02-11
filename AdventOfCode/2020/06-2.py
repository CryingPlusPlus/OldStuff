
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def every_in_group(group, c):
    for g in group:
        if c not in g:
            return False
    return True


def to_num(group):
    end = 0
    abc_clone = abc.copy()

    for g in group:
        for c in g:
            if c in abc_clone and every_in_group(group, c):
                abc_clone.remove(c)
                end += 1
    
    return end

def to_list_list(fh):
    end = []
    c = []

    for line in fh:
        line = line.split('\n')[0]
        if line == "":
            end.append(c)
            c = []
        else:
            c.append(line)

    end.append(c)
    return end


with open('data.txt', 'r') as fh:
    groups = to_list_list(fh)
    print(groups)

    groups = [to_num(g) for g in groups]
    print(groups)
    print(sum(groups))