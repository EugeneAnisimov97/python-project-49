import prompt
from brain_games.cli import welcome_user


def start_game(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.ABOUT_GAME)
    point = 0
    for _ in range(3):
        question, correct_answer = game.answer_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            point += 1
        else:
            print(f"'{user_answer}' in wrong answer ;(. Corrent answer was '{correct_answer}'.\nLet's try again, {name}!")  # noqa:E501
            break
        if point == 3:
            print(f'Congratulations, {name}!')