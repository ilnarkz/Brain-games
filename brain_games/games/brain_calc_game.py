from random import randint, choice
import brain_games.cli
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    name = brain_games.cli.welcome_user()
    counter = 0
    while counter < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        operator = choice('+-*')
        if operator == '+':
            correct_answer = num1 + num2
        if operator == '-':
            correct_answer = num1 - num2
        if operator == '*':
            correct_answer = num1 * num2
        print('Question: ' + (str(num1) + ' ' + operator + ' ' + str(num2)))
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


if __name__ == '__main__':
    main()
