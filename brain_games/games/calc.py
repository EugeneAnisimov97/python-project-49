import random


ABOUT_GAME = 'What is the result of the expression?'


def count_expression(number_first, number_second, expression):
    '''Вычисляем ответ выражения'''
    if expression == '+':
        answer = number_first + number_second
    if expression == '-':
        answer = number_first - number_second
    if expression == '*':
        answer = number_first * number_second
    return answer


def get_answer_question():
    '''Возвращаем значение для вопроса и ответ на вопрос'''
    number_first = random.randint(1, 10)
    number_second = random.randint(1, 10)
    expression = ['-', '+', '*']
    expression = random.choice(expression)
    return f'{number_first} {expression} {number_second}', str(count_expression(number_first, number_second, expression))  # noqa:E501
