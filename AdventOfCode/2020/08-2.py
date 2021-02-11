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
        acc = fix_instructions(insructions, 0)
        print(acc)


def fix_instructions(instructions, i):
    if instructions[i][0] == 'acc':
        return fix_instructions(instructions, i + 1)
    
    instructions[i][0] = 'jmp' if instructions[i][0] == 'nop' else 'nop'
    acc, done = find_acc(instructions)
    if done:
        return acc
    else:
        instructions[i][0] = 'jmp' if instructions[i][0] == 'nop' else 'nop'
        return fix_instructions(instructions, i + 1)
    
    

def find_acc(instructions):
    acc = 0
    i_list =[]
    i = 0

    while True:
        if i >= len(instructions):
            return acc, True
        if i in i_list:
            return acc, False
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