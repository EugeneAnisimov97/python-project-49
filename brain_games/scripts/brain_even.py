import random
import prompt
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def main():
    name = greet()
    point = 0
    for _ in range(3):
        number = random.randint(1, 99)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if number % 2 == 0 and user_answer == 'yes' or number % 2 != 0 and user_answer == 'no':    # noqa:E501
            print('Corrent!')
            point += 1
        else:
            if number % 2 == 0:
                correct_answer = 'yes'
                print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{correct_answer}'")  # noqa:E501
            elif number % 2 != 0:
                correct_answer = 'no'
                print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{correct_answer}'")  # noqa:E501
            break
        if point == 3:
            print(f'Congratulations, {name}!')
