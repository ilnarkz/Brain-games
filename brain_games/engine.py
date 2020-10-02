import prompt


def run(game=None):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    counter = 0
    while counter < 3:
        correct_answer, question = game.generate_answer_and_question()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        counter += 1
        error_string = "'{}' is wrong answer ;(. Correct answer was '{}'."
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(error_string.format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
