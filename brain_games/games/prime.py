import random


ABOUT_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    '''Определение простое ли значение number'''
    k = 0
    if number <= 1:
        return False
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    return k == 0


def get_answer_question():
    '''Возврат значения для ответа на вопрос'''
    number = random.randint(0, 99)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
