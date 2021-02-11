abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def to_num(line):
    end = 0
    abc_clone = abc.copy()

    for c in line:
        if c in abc_clone:
            abc_clone.remove(c)
            end += 1

    return end


def to_string_list(fh):
    end = []
    c = ""

    for line in fh:
        line = line.split('\n')[0]
        if line == "":
            end.append(c)
            c = ""
        else:
            c += line

    end.append(c)
    return end

with open('data.txt', 'r') as fh:
    groups = to_string_list(fh)
    groups = [to_num(line) for line in groups]
    print(sum(groups))

