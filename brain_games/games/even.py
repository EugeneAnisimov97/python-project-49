import random


ABOUT_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def answer_question():
    number = random.randint(1, 99)
    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
    
    
    
    
    
    
    # print(f'Question: {number}')
    # user_answer =     user_answer = prompt.string('Your answer: ')

    # if number % 2 == 0 and user_answer == 'yes' or number % 2 != 0 and user_answer == 'no':    # noqa:E501
    #     print('Correct!')
    # else:
    #     if number % 2 == 0:
    #         correct_answer = 'yes'
    #         print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{correct_answer}'.\nLet's try again, {name}!")  # noqa:E501
    #     elif number % 2 != 0:
    #         correct_answer = 'no'
    #         print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{correct_answer}'.\nLet's try again, {name}!")  # noqa:E501
    # if point == 3:
    #     print(f'Congratulations, {name}!')
