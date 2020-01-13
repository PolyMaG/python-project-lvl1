def calc():
    import prompt
    from random import randint, choice

    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    print()

    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    print()

    i = 1
    while i <= 3:
        number1 = randint(1, 99)
        number2 = randint(1, 99)
        operator = choice('+-*')

        if operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        else:
            result = number1 * number2

        question = str(number1) + ' {} '.format(operator) + str(number2)
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if int(answer) == result:
            print('Correct!')
        else:
            print("'{}'".format(answer) + " is wrong answer ;(.")
            print("Correct answer was " + "'{}'".format(result))
            print("Let's try again, {}!".format(name))
            return

        i += 1

    print("Congratulations, {}!".format(name))
