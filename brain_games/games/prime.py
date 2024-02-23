import random


ABOUT_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def answer_question():
    number = random.randint(1, 99)
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if k <= 0:
        corrent_answer = 'yes'
    else:
        corrent_answer = 'no'
    return number, corrent_answer
