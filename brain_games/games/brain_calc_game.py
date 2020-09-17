import brain_games.engine
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

def correct_answer():
    correct_answer = main()[0]
    return correct_answer

def question():
    num1 = main()[1]
    num2 = main()[2]
    operator = main()[3]
    return print('Question: ' + (str(num1) + ' ' + operator + ' ' + str(num2)))
