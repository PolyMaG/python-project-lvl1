def even():
    from random import randint
    from brain_games.games.cli import run
    from brain_games.games.ending import end

    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print()

    name = run()

    i = 1
    while i <= 3:
        number = randint(1, 99)
        if number % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        print('Question: {}'.format(number))

        i = end(i, result, name)
