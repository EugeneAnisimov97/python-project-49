import random
import prompt
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    return name


def make_string_progression():
    progression = []
    number = random.randrange(0, 100)
    step = random.randrange(1, 10)
    while len(progression) < 10:
        number += step
        if number not in progression:
            progression.append(number)
    progression.sort()
    return progression


def main():
    name = greet()
    point = 0
    invisible = '..'
    for _ in range(3):
        string_progression = ''
        progression = make_string_progression()
        index = random.randrange(0, 9)
        correct_number = progression[index]
        progression[index] = invisible
        for el in progression:
            string_progression += str(el)
            string_progression += ' '
        print(f'Question: {string_progression}')
        user_answer = prompt.integer('Your answer: ')
        if correct_number == user_answer:
            print('Correct!')
            point += 1
        else:
            print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{correct_number}'.\nLet's try again, {name}!")  # noqa:E501
            break
    if point == 3:
        print(f'Congratulation, {name}!')
