from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_answer_and_question():
    length_of_progression = 10
    num1 = randint(1, 100)
    step = randint(1, 10)
    position = randint(0, length_of_progression - 1)
    game_question = ''
    curr_index = 0
    while curr_index < length_of_progression:
        if curr_index != position:
            game_question = game_question + ' ' + str(num1 + step * curr_index)
            curr_index += 1
            continue
        else:
            game_question = game_question + ' ..'
            curr_index += 1
            continue
    correct_answer = num1 + step * position
    if game_question[0] == ' ':
        game_question = game_question[1:]
    question = game_question
    return correct_answer, question
