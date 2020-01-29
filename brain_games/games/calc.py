from random import randint, choice
GREETING = 'What is the result of the expression?'


def generate_data():
    number1 = randint(1, 99)
    number2 = randint(1, 99)
    operator = choice('+-*')

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    question = '{} {} {}'.format(str(number1), operator, str(number2))

    return question, str(result)
