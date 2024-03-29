import random


ABOUT_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    '''Определение чётное ли значение'''
    return number % 2 == 0


def get_answer_question():
    '''Возврат значения для ответа на вопрос'''
    number = random.randint(1, 99)
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
