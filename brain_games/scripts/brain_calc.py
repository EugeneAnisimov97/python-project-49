import random
import prompt
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    return name


def main():
    name = greet()
    point = 0
    for _ in range(3):
        number_first = random.randint(1, 10)
        number_second = random.randint(1, 10)
        count = random.randint(1, 3)
        match count:
            case 1:
                sum = number_first + number_second
                print(f'Question: {number_first} + {number_second}')
                user_answer = prompt.integer('Your answer: ')
                if sum == user_answer:
                    print('Correct!')
                    point += 1
                else:
                    print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{sum}'.\nLet's try again, {name}!")  # noqa:E501
                    break
            case 2:
                difference = number_first - number_second
                print(f'Question: {number_first} - {number_second}')
                user_answer = prompt.integer('Your answer: ')
                if difference == user_answer:
                    print('Correct!')
                    point += 1
                else:
                    print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{difference}'.\nLet's try again, {name}!")  # noqa:E501
                    break
            case 3:
                multiplication = number_first * number_second
                print(f'Question: {number_first} * {number_second}')
                user_answer = prompt.integer('Your answer: ')
                if multiplication == user_answer:
                    print('Correct!')
                    point += 1
                else:
                    print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{multiplication}'.\nLet's try again, {name}!")  # noqa:E501
                    break
        if point == 3:
            print(f'Congratulations, {name}!')

# def greet():
#     print('Welcome to the Brain Games!')
#     name = welcome_user()
#     print('What is the result of the expression?')
#     return name


# def sum():
#     number_first = random.randint(1, 10)
#     number_second = random.randint(1, 10)
#     sum = number_first + number_second
#     print(f'Question: {number_first} + {number_second}')
#     user_answer = int(prompt.string('Your answer: '))
#     if sum == user_answer:
#         print('Correct!')
#         return True
#     else:
#         print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{sum}'\nLet's try again, {name}!")  # noqa:E501
#         return False


# def difference():
#     number_first = random.randint(1, 10)
#     number_second = random.randint(1, 10)
#     difference = number_first - number_second
#     print(f'Question: {number_first} - {number_second}')
#     user_answer = int(prompt.string('Your answer: '))
#     if difference == user_answer:
#         print('Correct!')
#         return True
#     else:
#         print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{difference}'\nLet's try again, {name}!")  # noqa:E501
#         return False


# def multiplication():
#     number_first = random.randint(1, 10)
#     number_second = random.randint(1, 10)
#     multiplication = number_first * number_second
#     print(f'Question: {number_first} * {number_second}')
#     user_answer = int(prompt.string('Your answer: '))
#     if multiplication == user_answer:
#         print('Correct!')
#         return True
#     else:
#         print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{multiplication}'\nLet's try again, {name}!")  # noqa:E501
#         return False


# def main():
#     name = greet()
#     point = 0
#     for i in range(3):
#         count = random.randint(1, 3)
#         match count:
#             case 1:
#                 if sum() is False:
#                     break
#                 else:
#                     point += 1
#             case 2:
#                 if difference() is False:
#                     break
#                 else:
#                     point += 1
#             case 3:
#                 if multiplication() is False:
#                     break
#                 else:
#                     point += 1
#         if point == 3:
#             print(f'Congratulation, {name}!')
