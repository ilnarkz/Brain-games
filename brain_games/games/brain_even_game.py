from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def main():
    num = randint(1, 100)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = print('Question:' + str(num))
    return correct_answer, question
