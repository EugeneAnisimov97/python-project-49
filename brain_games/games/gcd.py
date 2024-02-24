import random


ABOUT_GAME = 'Find the greatest common divisor of given numbers.'


def is_nod(number_first, number_second):
    while number_first != number_second:
        if number_first > number_second:
            number_first = number_first - number_second
        else:
            number_second = number_second - number_first
    return number_second


def get_answer_question():
    number_first = random.randint(1, 20)
    number_second = random.randint(1, 20)
    return f'{number_first} {number_second}', str(is_nod(number_first, number_second))  # noqa:E501
