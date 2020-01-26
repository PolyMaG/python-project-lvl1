from random import randint, choice
GREETING = 'What is the result of the expression?'


def run():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    operator = choice('+-*')

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    result = str(result)
    question = '{} {} {}'.format(str(number1), operator, str(number2))

    return question, result
