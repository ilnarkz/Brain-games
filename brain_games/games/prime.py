from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    divisor = n - 1
    while divisor > 1:
        if n % divisor == 0:
            return False
            break
        else:
            divisor -= 1
    return True


def generate_answer_and_question():
    num = randint(1, 100)
    if is_prime(num) is False:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    question = str(num)
    return correct_answer, question
