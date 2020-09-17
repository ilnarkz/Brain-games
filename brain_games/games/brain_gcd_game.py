import brain_games.engine
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def main():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    def pair_of_numbers(num1, num2):
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return num1
    question = print('Question: ' + str(num1) + ' ' + str(num2))
    correct_answer = pair_of_numbers(num1, num2)
    return correct_answer, question
