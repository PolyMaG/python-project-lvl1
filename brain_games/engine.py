def engine(game):
    import prompt

    print('Welcome to the Brain Games!')
    print(game.GREETING)
    print()

    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print()

    roundscount = 3
    i = 1
    while i <= roundscount:
        question, result = game.generate_data()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer == result:
            if i == roundscount:
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
