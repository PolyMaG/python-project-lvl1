def prime():
    from random import randint
    from brain_games.games.cli import run
    from brain_games.games.ending import end

    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print()

    name = run()

    i = 1
    while i <= 3:
        number = randint(1, 999)
        if number < 2:
            result = 'no'
        elif number == 2:
            result = 'yes'
        else:
            divider = 2
            while divider < number:
                if number % divider == 0:
                    result = 'no'
                    break
                divider += 1
                result = 'yes'

        print('Question: {}'.format(number))

        i = end(i, result, name)
