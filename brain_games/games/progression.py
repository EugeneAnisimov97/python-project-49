import random


ABOUT_GAME = 'What number is missing in the progression?'


def criating_progression():
    '''Создаем массив с шагом step и сортируем его по возрастанию'''
    progression = []
    number = random.randrange(0, 100)
    step = random.randrange(1, 10)
    while len(progression) < 10:
        number += step
        progression.append(number)
    return progression


def get_answer_question():
    '''Возвращаем значение для вопроса и ответ на вопрос'''
    invisible = '..'
    string_progression = ''
    progression = criating_progression()
    index = random.randrange(0, 9)
    correct_number = progression[index]
    progression[index] = invisible
    string_progression = [str(sl) for sl in progression]
    result_progression = ' '.join(string_progression)
    return result_progression, str(correct_number)
