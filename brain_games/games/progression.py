from random import randint
GREETING = 'What number is missing in the progression?'
length_progression = 10


def run():
    start = randint(1, 10)
    step = randint(1, 10)
    index_hidden_number = randint(0, length_progression - 1)
    progression = []
    j = 1
    while j <= length_progression:
        progression = progression + [start + (step * j)]
        j += 1
    result = str(progression[index_hidden_number])
    progression[index_hidden_number] = '..'
    progression = str(progression)
    progression = progression.strip('[]')
    progression = progression.replace(',', '')
    question = progression.replace("'", "")

    return question, result
