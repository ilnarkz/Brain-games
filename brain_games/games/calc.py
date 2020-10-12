from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def generate_answer_and_question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice('-+*')
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    question = str(num1) + ' ' + operator + ' ' + str(num2)
    return correct_answer, question
