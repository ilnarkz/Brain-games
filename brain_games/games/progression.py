from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_answer_and_question():
    num1 = randint(1, 100)
    step = randint(1, 10)
    position = randint(0, 9)
    str_question = ''
    curr_index = 0
    last_index = 9
    while curr_index <= last_index:
        if curr_index == 0 and position == 0:
            str_question = '..'
            curr_index += 1
            continue
        if curr_index == 0 and position != 0:
            str_question = str(num1)
            curr_index += 1
            continue
        if curr_index != 0 and curr_index != position:
            str_question = str_question + ' ' + str(num1 + step * curr_index)
            curr_index += 1
            continue
        else:
            str_question = str_question + ' ..'
            curr_index += 1
            continue
    if position == 0:
        correct_answer = num1
    else:
        correct_answer = num1 + step * position
    question = str_question
    return correct_answer, question
