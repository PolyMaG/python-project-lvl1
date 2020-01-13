def even():
    import prompt
    from random import randint
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    print()

    i = 1
    while i <= 3:
        number = randint(1, 99)
        if number % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print("'{}'".format(answer) + " is wrong answer ;(.")
            print("Correct answer was " + "'{}'".format(result))
            print("Let's try again, {}!".format(name))
            return
        i += 1

    print('Congratulations, {}!'.format(name))
