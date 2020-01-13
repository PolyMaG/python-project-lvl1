def gcd():
    import prompt
    from random import randint

    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    print()

    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    print()

    i = 1
    while i <= 3:
        number1 = randint(1, 999)
        number2 = randint(1, 99)
        max_number = max(number1, number2)
        min_number = min(number1, number2)

        gcd = 1
        while gcd <= min_number:
            if max_number % gcd == 0 and min_number % gcd == 0:
                result = gcd
            gcd += 1

        print('Question: {}, {}'.format(number1, number2))
        answer = prompt.string('Your answer: ')
        if int(answer) == result:
            print('Correct!')
        else:
            print("'{}'".format(answer) + " is wrong answer ;(.")
            print("Correct answer was " + "'{}'".format(result))
            print("Let's try again, {}!".format(name))
            return

        i += 1

    print("Congratulations, {}!".format(name))
