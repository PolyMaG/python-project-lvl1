greeting = 'What is the result of the expression?'


def round():
    from random import randint, choice

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

    return question, result
