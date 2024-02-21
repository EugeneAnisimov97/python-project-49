# import random
# import prompt
# from brain_games.games.engine import greet, lose, ask_user_answer, congratulations, correct

# def is_prime():
#     number = random.randint(1, 99)
#     print(f'Question: {number}')
#     k = 0
#     for i in range(2, number // 2 + 1):
#         if (number % i == 0):
#             k = k + 1
#     if k <= 0:
#         correct_answer = 'yes'
#     else:
#         correct_answer = 'no'
#     return correct_answer


# def main():
#     name = greet()
#     point = 0
#     for _ in range(3):
#         correct_answer = is_prime()
#         user_answer = ask_user_answer()
#         if user_answer == correct_answer:
#             correct()
#         else:
#             lose(user_answer, correct_answer, name)
#             break
#     if point == 3:
#         congratulations(name)
