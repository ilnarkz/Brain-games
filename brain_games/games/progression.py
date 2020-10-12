from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_answer_and_question():
    length_of_progression = 10
    num1 = randint(1, 100)
    step = randint(1, 10)
    position = randint(0, length_of_progression - 1)
    gen_question = ''
    curr_index = 0
    while curr_index < length_of_progression:
        if curr_index != position:
            gen_question = gen_question + ' ' + str(num1 + step * curr_index)
            curr_index += 1
            continue
        else:
            gen_question = gen_question + ' ..'
            curr_index += 1
            continue
    if position == 0:
        correct_answer = num1
    else:
        correct_answer = num1 + step * position
    if gen_question[0] == ' ':
        gen_question = gen_question[1:]
    if gen_question[-1] == ' ':
        gen_question = gen_question[:-2]
    question = gen_question
    return correct_answer, question
