from random import randint
GREETING = 'What number is missing in the progression?'
length_progression = 10


def generate_data():
    start = randint(1, 10)
    step = randint(1, 10)
    hidden_number = randint(0, length_progression - 1)
    question = ''
    j = 0
    while j < length_progression:
        if question:
            question += ' '
        if j != hidden_number:
            question = question + str((start + (step * j)))
            j += 1
        else:
            question += '..'
            result = str(start + (step * j))
            j += 1

    return question, result
