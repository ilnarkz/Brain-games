from random import randint
import brain_games.cli
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    name = brain_games.cli.welcome_user()
    counter = 0
    while counter < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)

        def pair_of_numbers(num1, num2):
            while num1 != num2:
                if num1 > num2:
                    num1 = num1 - num2
                else:
                    num2 = num2 - num1
            return num1
        correct_answer = pair_of_numbers(num1, num2)
        print('Question: ' + str(num1) + ' ' + str(num2))
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
