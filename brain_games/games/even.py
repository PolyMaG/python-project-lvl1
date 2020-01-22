greeting = 'Answer "yes" if number even otherwise answer "no".'


def round():
    from random import randint

    number = randint(1, 99)
    question = number
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    return question, result
