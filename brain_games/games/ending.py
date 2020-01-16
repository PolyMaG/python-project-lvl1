def end(i, result, name):
    import prompt

    answer = prompt.string('Your answer: ')
    if answer == result:
        if i == 3:
            print('Correct!')
            print("Congratulations, {}!".format(name))
            i = 4
            return(i)
        else:
            print('Correct!')
            i += 1
            return(i)
    else:
        print("'{}'".format(answer) + " is wrong answer ;(.")
        print("Correct answer was " + "'{}'".format(result))
        print("Let's try again, {}!".format(name))
        i = 4
        return(i)
