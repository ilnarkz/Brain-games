from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    divisor = 2
    while divisor <= n / 2:
        if n % divisor == 0:
            return False
            break
        else:
            divisor += 1
    return True


def generate_answer_and_question():
    num = randint(1, 100)
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = str(num)
    return correct_answer, question
