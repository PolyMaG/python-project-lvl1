from random import randint
GREETING = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    max_number = max(number1, number2)
    min_number = min(number1, number2)

    gcd = 1
    while gcd <= min_number:
        if max_number % gcd == 0 and min_number % gcd == 0:
            result = str(gcd)
        gcd += 1
    return result


def generate_data():
    number1 = randint(1, 99)
    number2 = randint(1, 99)

    result = get_gcd(number1, number2)

    question = '{} {}'.format(number1, number2)

    return question, result
