def progression():
    import prompt
    from random import randint

    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    print()

    name = prompt.string('May I have your name? ')
    print('Hello, {}!'. format(name))
    print()

    i = 1
    while i <= 3:
        start = randint(1, 10)
        step = randint(1, 10)
        index_hidden_number = randint(0, 9)
        c = start
        progression = [start]
        j = 1
        while j < 10:
            c = c + step
            progression = progression + [c]
            j += 1
        result = progression[index_hidden_number]
        progression[index_hidden_number] = '..'
        progression = str(progression)
        progression = progression.strip('[]')
        progression = progression.replace(',', '')
        question = progression.replace("'", "")

        print('Question: {}'.format(question))
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
