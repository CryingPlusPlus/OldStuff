print('schreib was')
a = input()
s = a.encode("utf-8").hex()
print(s)
print('')
output = ''
end = []
for b in s:
    b == '0'
    if b.isdecimal():
        output += b
    elif b == 'a':
        output += ' Äpfel'
        end.append(output)
        output = ''
    elif b == 'b':
        output += ' Bananen'
        end.append(output)
        output = ''
    elif b == 'c':
        output += ' Citrusfrüchte'
        end.append(output)
        output = ''
    elif b == 'd':
        output += ' Datteln'
        end.append(output)
        output = ''
    elif b == 'e':
        output += ' Erdbeeren'
        end.append(output)
        output = ''
    elif b == 'f':
        output += ' Feigen'
        end.append(output)
        output = ''

for e in end:
    print(e)