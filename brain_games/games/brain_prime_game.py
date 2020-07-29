
from random import randint
import brain_games.cli
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = brain_games.cli.welcome_user()
    counter = 0
    while counter < 3:
        num = randint(1, 100)
        divisor = num - 1
        while divisor > 1:
            if num % divisor == 0:
                correct_answer = 'yes'
                break
            else:
                divisor -= 1
        if divisor == 1:
            correct_answer = 'no'
        print('Question:' + str(num))
        answer = prompt.string('Your answer: ')
        counter += 1
        error_string = "'{}' is wrong answer ;(. Correct answer was '{}'."
        if answer == correct_answer:
            print('Correct!')
        else:
            print(error_string.format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    if counter == 3:
        print('Congratulations, {}!'.format(name))


