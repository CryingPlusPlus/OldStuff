import pyinputplus as pyip, random

a = 10
correctAnswers = 0
trials = 0
timeout = False
while True:
    if trials < 3 and not timeout:
        numone = random.randint(0, a)
        numtwo = random.randint(0, a)
        print(str(numone) + ' x ' + str(numtwo))
        answer = pyip.inputInt(timeout=8, default=-1)
        if answer == numone * numtwo:
            print('Correct')
            correctAnswers += 1
            trials = 0
        elif answer != -1:
            print('incorrect')
            trials += 1
        else:
            timout = True
    else:
        if timeout:
            print('You have timed out, but you have: ' + str(correctAnswers) + ' right')
        elif trials >=3:
            print('To many wrong, but you have: ' + str(correctAnswers) + ' right')

        print('Continue? ')
        answer = pyip.inputYesNo()
        if answer == 'yes':
            timout = False
            trials = 0
            correctAnswers = 0
            continue
        else:
            break
