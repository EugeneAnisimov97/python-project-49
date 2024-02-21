# import random
# import prompt
# from brain_games.games.engine import greet, lose, ask_user_answer, congratulations, correct


# def gcd(number_first, number_second):
#     while number_first != number_second:
#         if number_first > number_second:
#             number_first = number_first - number_second
#         else:
#             number_second = number_second - number_first
#     return number_second


# def main():
#     name = greet()
#     point = 0
#     correct_answer = gcd(number_first, number_second)
#     for _ in range(3):
#         number_first = random.randint(1, 20)
#         number_second = random.randint(1, 20)
#         print(f'Question: {number_first} {number_second}')
#         user_answer = ask_user_answer()
#         if gcd(number_first, number_second) == user_answer:
#             correct()
#         else:
#             lose(user_answer, correct_answer, name)
#             break
#     if point == 3:
#         congratulations(name)
