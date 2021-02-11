from pprint import pprint

def to_list(fh):
    instructions = []
    for line in fh:
        line = line.split('\n')[0]
        ins = line.split(' ')
        instructions.append([ins[0], int(ins[1])])
    
    return instructions

def main():
    with open('data.txt', 'r') as fh:
        insructions = to_list(fh)
        acc = find_acc(insructions)
        print(acc)


def find_acc(instructions):
    acc = 0
    i_list =[]
    i = 0

    while True:
        print(instructions[i])

        if i in i_list:
            return acc
        i_list.append(i)
        
        if instructions[i][0] == 'acc':
            acc += instructions[i][1]
            i += 1
            continue
        
        if instructions[i][0] == 'jmp':
            i += instructions[i][1]
            continue
        
        if instructions[i][0] == 'nop':
            i += 1
            continue


if __name__ == '__main__':
    main()