def even():
    import prompt
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))

    number1 = 15
    number2 = 6
    number3 = 7

    print('Question: {}'.format(number1))
    answer1 = prompt.string('Your answer: ')
    if answer1 == 'no':
        print('Correct!')
        print('Question: {}'.format(number2))
        answer2 = prompt.string('Your answer: ')
    else:
        print("'{}'".format(answer1) + " is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, {}!".format(name))
        return

    if answer2 == 'yes':
        print('Correct!')
        print('Question: {}'.format(number3))
        answer3 = prompt.string('Your answer: ')
    else:
        print("'{}'".format(answer2) + " is wrong answer ;(. Correct answer was 'yes'.")
        print("Let's try again, {}!".format(name))
        return

    if answer3 == 'no':
        print('Correct!')
        print('Congratulations, {}!'.format(name))
    else:
        print("'{}'".format(answer3) + " is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, {}!".format(name))
