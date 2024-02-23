import random


ABOUT_GAME = 'What is the result of the expression?'


def answer_question():
        number_first = random.randint(1, 10)
        number_second = random.randint(1, 10)
        count = random.randint(1, 3)
        match count:
            case 1:
                sum = number_first + number_second
                return f'{number_first} + {number_second}', str(sum)

            case 2:
                difference = number_first - number_second
                return f'{number_first} - {number_second}', str(difference)

            case 3:
                multiplication = number_first * number_second
                return f'{number_first} * {number_second}', str(multiplication)
