import random


ABOUT_GAME = 'What is the result of the expression?'


def expression(number_first, number_second, sl_for_expression):
    '''вычисляем ответ выражения'''
    if sl_for_expression == '+':
        answer = number_first + number_second
        return answer
    if sl_for_expression == '-':
        answer = number_first - number_second
        return answer
    if sl_for_expression == '*':
        answer = number_first * number_second
        return answer


def get_answer_question():
    number_first = random.randint(1, 10)
    number_second = random.randint(1, 10)
    symbol = ['-', '+', '*']
    sl_for_expression = random.choice(symbol)
    if sl_for_expression == '+':
        return f'{number_first} + {number_second}', str(expression(number_first, number_second, sl_for_expression))  # noqa:E501
    if sl_for_expression == '-':
        return f'{number_first} - {number_second}', str(expression(number_first, number_second, sl_for_expression))  # noqa:E501
    if sl_for_expression == '*':
        return f'{number_first} * {number_second}', str(expression(number_first, number_second, sl_for_expression))  # noqa:E501
