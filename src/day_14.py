""" Day 14 of Coding Challenges for guessing who has higher or lower followers"""
import random

from src.constants.ascii_art import HIGHER_LOWER, VS
from src.constants.values import CELEBRITIES


def get_celebrity_info(celebrity: dict[str, str]) -> str:
    """ Get the name, description and country of a celebrity"""
    return f"{celebrity["name"]}, a {celebrity["description"]} from {celebrity["country"]}."


def get_next_celebrity(celebrities: list[dict[str, str | int]]) -> dict[str, str | int]:
    """ Get the next celebrity from the list"""
    return celebrities.pop()


def collect_guess(celebrity_1: dict[str, str | int], celebrity_2: dict[str, str | int]) -> str:
    """ Collect the guess of which celebrity is more popular"""
    print(f"Compare A: {get_celebrity_info(celebrity_1)}"
          f"{VS}"
          f"Against B: {get_celebrity_info(celebrity_2)}")
    return input("Who has more followers? Type \'A\' or \'B\': ")


def check_answer(guess, celebrity_1, celebrity_2):
    """ Check answer for which celebrity has more followers"""
    if celebrity_1["follower_count"] > celebrity_2["follower_count"]:
        return guess == "A"

    return guess == "B"


def higher_lower():
    """ Higher or Lower"""
    print(HIGHER_LOWER)
    celebrities = CELEBRITIES
    random.shuffle(celebrities)

    correct_guesses = 0
    celebrity_1 = get_next_celebrity(celebrities)
    celebrity_2 = get_next_celebrity(celebrities)
    correct = True
    while correct:
        guess = collect_guess(celebrity_1, celebrity_2)
        correct = check_answer(guess, celebrity_1, celebrity_2)
        if correct:
            correct_guesses += 1
            print(f"Correct answer, that is {correct_guesses} correct guesses in a row")
            celebrity_1 = celebrity_2
            celebrity_2 = get_next_celebrity(celebrities)
        else:
            print(f"Incorrect answer! You made {correct_guesses} correct guesses in a row")
