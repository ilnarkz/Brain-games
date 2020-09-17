from random import randint, choice
import brain_games.cli
import prompt


def num_generate():
    return randint(1, 100)

def operator_generate():
    return choice('+-*')

def step_generate():
    return randint(1, 10)

def position_generate():
    return randint(0, 9)

def run(game=None):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = brain_games.cli.welcome_user()
    counter = 0
    while counter < 3:
        correct_answer, answer = game.main()
        answer = prompt.string('Your answer: ')
        counter += 1
        error_string = "'{}' is wrong answer ;(. Correct answer was '{}'."
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(error_string.format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    if counter == 3:
        print('Congratulations, {}!'.format(name))

