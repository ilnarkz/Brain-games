from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def main():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = choice('-+*')
    if operator == '+':
        correct_answer = num1 + num2
    if operator == '-':
        correct_answer = num1 - num2
    if operator == '*':
        correct_answer = num1 * num2
    question = print('Question: ' + (str(num1) + ' ' + operator + ' ' + str(num2)))
    return correct_answer, question
