def engine(game):
    import prompt

    print('Welcome to the Brain Games!')
    print(game.GREETING)
    print()

    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print()

    rounds = 3
    i = 1
    while i <= rounds:
        question, result = game.run()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == result:
            if i == rounds:
                print('Correct!')
                print("Congratulations, {}!".format(name))
                return
            else:
                print('Correct!')
                i += 1

        else:
            print("'{}'".format(answer) + " is wrong answer ;(.")
            print("Correct answer was " + "'{}'".format(result))
            print("Let's try again, {}!".format(name))
            return
