import random


ABOUT_GAME = 'What number is missing in the progression?'


def make_string_progression():
    progression = []
    number = random.randrange(0, 100)
    step = random.randrange(1, 10)
    while len(progression) < 10:
        number += step
        if number not in progression:
            progression.append(number)
    progression.sort()
    return progression


def answer_question():
    invisible = '..'
    string_progression = ''
    progression = make_string_progression()
    index = random.randrange(0, 9)
    correct_number = progression[index]
    progression[index] = invisible
    for el in progression:
        string_progression += str(el)
        string_progression += ' '
    return string_progression, str(correct_number)
