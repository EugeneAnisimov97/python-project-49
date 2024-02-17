import random
import prompt
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def isPrime():
    number = random.randint(1, 99)
    print(f'Question: {number}')
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if k <= 0:
        corrent_answer = 'yes'
    else:
        corrent_answer = 'no'
    return corrent_answer


def main():
    name = greet()
    point = 0
    for _ in range(3):
        corrent_answer = isPrime()
        user_answer = prompt.string('Your answer: ')
        if user_answer == corrent_answer:
            print('Corrent!')
            point += 1
        else:
            print(f"'{user_answer}' in wrong answer ;(. Corrent answer was {corrent_answer}")  # noqa:E501
            break
    if point == 3:
        print(f'Congratulation, {name}!')
