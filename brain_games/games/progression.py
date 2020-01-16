def progression():
    from random import randint
    from brain_games.games.cli import run
    from brain_games.games.ending import end

    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    print()

    name = run()

    i = 1
    while i <= 3:
        start = randint(1, 10)
        step = randint(1, 10)
        index_hidden_number = randint(0, 9)
        next_step = start
        progression = [start]
        j = 1
        while j < 10:
            next_step = next_step + step
            progression = progression + [next_step]
            j += 1
        result = str(progression[index_hidden_number])
        progression[index_hidden_number] = '..'
        progression = str(progression)
        progression = progression.strip('[]')
        progression = progression.replace(',', '')
        question = progression.replace("'", "")

        print('Question: {}'.format(question))

        i = end(i, result, name)
