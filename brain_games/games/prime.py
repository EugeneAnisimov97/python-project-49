import random


ABOUT_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    k = 0
    if number == 1:
        k = 1
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    return k <= 0


def get_answer_question():
    number = random.randint(0, 10)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
