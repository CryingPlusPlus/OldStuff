import pyinputplus as pyip, random

a = 10
done = 0
while True:
    numone = random.randint(0, a)
    numtwo = random.randint(0, a)
    print('What ist ' + str(numone) + ' times ' + str(numtwo))
    trial = pyip.inputNum(timeout=10, default=-1)
    if trial == numone * numtwo:
        print('GJ')
        if done != 0 and done % 10 == 0:
            a += 10
        done += 1
    elif trial == -1:
        print('You have timed out')
        print('You have made it to Level: ' + str(done))
        if pyip.inputYesNo('Try Again?') == 'yes':
            done = 0
            a = 10
            continue
        else:
            break
    else:
        print('You have made it to Level: ' + str(done))
        if pyip.inputYesNo('Try Again?') == 'yes':
            done = 0
            a = 10
            continue
        else:
            break

print('Goodbye')
