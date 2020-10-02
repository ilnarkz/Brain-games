from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_answer_and_question():
    num1 = randint(1, 100)
    step = randint(1, 10)
    position = randint(0, 9)
    str_question = ''
    current_index = 0
    last_index = 9
    while current_index <= last_index:
        if current_index == 0 and position == 0:
            str_question = '..'
            current_index += 1
            continue
        if current_index == 0 and position != 0:
            str_question = str(num1)
            current_index += 1
            continue
        if current_index != 0 and current_index != position:
            str_question = str_question + ' ' + str(num1 + step * current_index)
            current_index += 1
            continue
        else:
            str_question = str_question + ' ..'
            current_index += 1
            continue
    if position == 0:
        correct_answer = num1
    else:
        correct_answer = num1 + step * position
    question = str_question
    return correct_answer, question
