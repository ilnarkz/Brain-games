from random import randint
from brain_games.cli import welcome_user
import prompt
import brain_games.scripts.brain_games


def main():
    brain_games.scripts.brain_games.main()
    name = brain_games.cli.welcome_user()
    counter = 0
    while counter < 3:
        num = randint(1, 100)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question:' + str(num))
        answer = prompt.string('Your answer: ')
        counter += 1
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    if counter == 3:
        print('Congratulations, {}'.format(name))


if __name__ == '__main__':
    main()
