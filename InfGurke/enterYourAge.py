while True:
    print('Please enter your Age: ')
    try:
        age = int(input())
        break
    except:
        print('Thats no Age')
        continue

print('Ur Age is: ' + str(age))