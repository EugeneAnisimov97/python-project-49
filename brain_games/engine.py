import prompt
from brain_games.cli import welcome_user


def start_game(game):
    '''Запускает игру описанную в модуле game'''
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.ABOUT_GAME)
    for _ in range(3):
        question, correct_answer = game.get_answer_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{correct_answer}'.\nLet's try again, {name}!")  # noqa:E501
            return
    print(f'Congratulations, {name}!')
