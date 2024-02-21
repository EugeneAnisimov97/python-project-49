# import random
# import prompt
# from brain_games.engine import greet, lose, ask_user_answer, congratulations, correct


# def main():
#     name = greet()
#     point = 0
#     for _ in range(3):
#         number_first = random.randint(1, 10)
#         number_second = random.randint(1, 10)
#         count = random.randint(1, 3)
#         match count:
#             case 1:
#                 correct_answer = number_first + number_second
#                 print(f'Question: {number_first} + {number_second}')
#                 user_answer = ask_user_answer()
#                 if correct_answer == user_answer:
#                     correct()
#                     point += 1
#                 else:
#                     lose(user_answer, correct_answer, name)
#                     break
#             case 2:
#                 correct_answer = number_first - number_second
#                 print(f'Question: {number_first} - {number_second}')
#                 user_answer = ask_user_answer()
#                 if correct_answer == user_answer:
#                     correct()
#                     point += 1
#                 else:
#                     lose(user_answer, correct_answer, name)
#                     break
#             case 3:
#                 correct_answer = number_first * number_second
#                 print(f'Question: {number_first} * {number_second}')
#                 user_answer = ask_user_answer()
#                 if correct_answer == user_answer:
#                     correct()
#                     point += 1
#                 else:
#                     lose(user_answer, correct_answer, name)
#                     break
#         if point == 3:
#             congratulations(name)
