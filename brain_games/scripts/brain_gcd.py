import random
import prompt
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    return name


def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


def main():
    name = greet()
    point = 0
    for _ in range(3):
        number_first = random.randint(1, 20)
        number_second = random.randint(1, 20)
        print(f'Question: {number_first} {number_second}')
        user_answer = int(prompt.string('Your answer: '))
        if gcd(number_first, number_second) == user_answer:
            print('Correct!')
            point += 1
        else:
            print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{gcd(number_first, number_second)}'\nLet's try again, {name}!")  # noqa:E501
            break
    if point == 3:
            print(f'Congratulation, {name}!')