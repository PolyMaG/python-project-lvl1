from random import randint
GREETING = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


def run():
    number = randint(1, 999)
    question = number
    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'

    return question, result
