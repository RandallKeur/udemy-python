""" Day 14 of Coding Challenges for guessing who has higher or lower followers"""
import random

from src.constants.ascii_art import HIGHER_LOWER, VS
from src.shared_files.celebrities import CELEBRITIES


def get_celebrity_info(celebrity: dict[str, str]) -> str:
    return f'{celebrity['name']}, a {celebrity['description']} from {celebrity['country']}.'


def get_next_celebrity(celebrities: list[dict[str, str | int]], correct_guesses: int) -> dict[str, str | int]:
    return celebrities[correct_guesses+2]


def higher_lower():
    print(HIGHER_LOWER)
    celebrities = CELEBRITIES
    random.shuffle(celebrities)

    correct_guesses = 0
    celebrity_1 = celebrities[0]
    celebrity_2 = celebrities[1]
    correct = True
    while correct:
        print(f'Compare A: {get_celebrity_info(celebrity_1)}'
              f'{VS}'
              f'Against B: {get_celebrity_info(celebrity_2)}')
        guess = input('Who has more followers? Type \'A\' or \'B\': ')
        if celebrity_1['follower_count'] > celebrity_2['follower_count']:
            answer = 'A'
            celebrity_2 = get_next_celebrity(celebrities, correct_guesses)
        else:
            answer = 'B'
            celebrity_1 = get_next_celebrity(celebrities, correct_guesses)
        if guess == answer:
            correct_guesses += 1
            print(f'Correct answer, that is {correct_guesses} correct guesses in a row')
        else:
            print(f'Incorrect answer! You made {correct_guesses} correct guesses in a row')
            correct = False

