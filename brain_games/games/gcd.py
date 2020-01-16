def gcd():
    from random import randint
    from brain_games.games.cli import run
    from brain_games.games.ending import end

    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    print()

    name = run()

    i = 1
    while i <= 3:
        number1 = randint(1, 99)
        number2 = randint(1, 99)
        max_number = max(number1, number2)
        min_number = min(number1, number2)

        gcd = 1
        while gcd <= min_number:
            if max_number % gcd == 0 and min_number % gcd == 0:
                result = str(gcd)
            gcd += 1

        print('Question: {}, {}'.format(number1, number2))

        i = end(i, result, name)
