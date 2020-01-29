from random import randint
GREETING = 'Answer "yes" if number even. Otherwise answer "no".'


def generate_data():
    question = randint(1, 99)
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    return question, result
