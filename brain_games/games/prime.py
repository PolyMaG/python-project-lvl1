greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def round():
    from random import randint

    number = randint(1, 999)
    question = number

    def is_prime(number):
        if number < 2:
            return False

        divider = 2
        while divider < number:
            if number % divider == 0:
                return False
            divider += 1
        return True

    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'

    return question, result
