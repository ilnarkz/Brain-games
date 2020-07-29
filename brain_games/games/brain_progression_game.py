from random import randint, choice
import brain_games.cli
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    name = brain_games.cli.welcome_user()
    counter = 0
    while counter < 3:
        num1 = randint(1, 100)
        step = randint(1, 10)
        position = randint(0, 9)
        string_question = ''
        index = 0
        while index < 10:
            if index == 0 and position == 0:
                string_question = '..'
                index += 1
                continue
            if index == 0 and position != 0:
                string_question = str(num1)
                index += 1
                continue
            if index != 0 and index != position:
                string_question = string_question + ' ' + str(num1 + step * index)
                index += 1
                continue
            else:
                string_question = string_question + ' ..'
                index += 1
                continue
        if position == 0: 
            correct_answer = num1
        else:
            correct_answer = num1 + step * position
        print('Question: ' + string_question)
        answer = prompt.string('Your answer: ')
        counter += 1
        error_string = "'{}' is wrong answer ;(. Correct answer was '{}'."
        if int(answer) == correct_answer:
            print('Correct!')
        else:
            print(error_string.format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    if counter == 3:
        print('Congratulations, {}!'.format(name))
