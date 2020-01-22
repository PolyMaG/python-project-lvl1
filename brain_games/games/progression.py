greeting = 'What number is missing in the progression?'


def round():
    from random import randint

    start = randint(1, 10)
    step = randint(1, 10)
    length_progression = 10
    index_hidden_number = randint(0, length_progression - 1)
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

    return question, result
