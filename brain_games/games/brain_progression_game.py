from random import randint
import brain_games.engine
import prompt


DESCRIPTION = 'What number is missing in the progression?'

def main():
    num1 = randint(1, 100)
    step = randint(1, 10)
    position = randint(0, 9)
    str_question = ''
    index = 0
    while index < 10:
        if index == 0 and position == 0:
            str_question = '..'
            index += 1
            continue
        if index == 0 and position != 0:
            str_question = str(num1)
            index += 1
            continue
        if index != 0 and index != position:
            str_question = str_question + ' ' + str(num1 + step * index)
            index += 1
            continue
        else:
            str_question = str_question + ' ..'
            index += 1
            continue
    if position == 0:
        correct_answer = num1
    else:
        correct_answer = num1 + step * position
    question = print('Question: ' + str_question)
    return correct_answer, question
