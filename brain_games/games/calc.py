def calc():
    from random import randint, choice
    from brain_games.games.cli import run
    from brain_games.games.ending import end

    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    print()

    name = run()

    i = 1
    while i <= 3:
        number1 = randint(1, 99)
        number2 = randint(1, 99)
        operator = choice('+-*')

        if operator == '+':
            result = str(number1 + number2)
        elif operator == '-':
            result = str(number1 - number2)
        else:
            result = str(number1 * number2)

        question = str(number1) + ' {} '.format(operator) + str(number2)
        print('Question: {}'.format(question))

        i = end(i, result, name)
