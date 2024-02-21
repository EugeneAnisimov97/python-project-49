# import random
# import prompt
# from brain_games.games.engine import greet, lose, ask_user_answer, congratulations, correct


# def make_string_progression():
#     progression = []
#     number = random.randrange(0, 100)
#     step = random.randrange(1, 10)
#     while len(progression) < 10:
#         number += step
#         if number not in progression:
#             progression.append(number)
#     progression.sort()
#     return progression


# def main():
#     name = greet()
#     point = 0
#     invisible = '..'
#     for _ in range(3):
#         string_progression = ''
#         progression = make_string_progression()
#         index = random.randrange(0, 9)
#         correct_answer = progression[index]
#         progression[index] = invisible
#         for el in progression:
#             string_progression += str(el)
#             string_progression += ' '
#         print(f'Question: {string_progression}')
#         user_answer = ask_user_answer()
#         if correct_answer == user_answer:
#             correct()
#         else:
#             lose(user_answer, correct_answer, name)
#             break
#     if point == 3:
#         congratulations(name)