import brain_games.engine
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def main():
    num = randint(1, 100)
    divisor = num - 1
    while divisor > 1:
        if num % divisor == 0:
            correct_answer = 'no'
            break
        else:
            divisor -= 1
    if divisor == 1:
        correct_answer = 'yes'
    question = print('Question:' + str(num))
    return correct_answer, question
