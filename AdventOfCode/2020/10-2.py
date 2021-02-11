def make_rules(jolts):
    rules = {jolts[-1] : jolts[-1]}
    for el in jolts:
        temp = []
        for i in range(1, 4):
            if el + i in jolts:
                temp.append(el + i)
        rules[el] = temp
    return rules

def reader():
    end = []
    with open('data.txt', 'r') as fh:
        for line in fh:
            line = line.split('\n')[0]
            end.append(int(line))
    end.append(0)
    end.append(max(end) + 3)
    end.sort()
    return end

make_worths = lambda jolts : {max(jolts) : 1}

def all_in(worths, rule):
    for el in rule:
        if el not in worths:
            return False
    return True

def append_worths(worths, rules):
    for key, val in rules.items():
        if all_in(worths, val):
            temp = 0
            for el in val:
                temp += worths[el]
            worths[key] = temp
            rules.pop(key)
            return append_worths(worths, rules)
    return worths

def main():
    jolts = reader()
    rules = make_rules(jolts)

    rules.pop(max(jolts))
    worths = make_worths(jolts)

    worths = append_worths(worths, rules)
    print(worths)


if __name__ == "__main__":
    main()