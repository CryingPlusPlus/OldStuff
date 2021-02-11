for i in range(1, 101):
    answer = ''

    if i % 3 == 0:
        answer += 'Fizz'
    if i % 5 == 0:
        answer += 'Buzz'

    print(answer or i)
