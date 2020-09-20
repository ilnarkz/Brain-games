import brain_games.cli
import prompt


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
