from random import randint
GREETING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question < 2:
        return False

    divider = 2
    while divider <= question / 2:
        if question % divider == 0:
            return False
        divider += 1
    return True


def generate_data():
    question = randint(1, 999)
    if is_prime(question):
        result = 'yes'
    else:
        result = 'no'

    return question, result
