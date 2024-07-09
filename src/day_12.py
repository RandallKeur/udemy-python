""" Day 12 of Coding Challenges for Number Guessing"""
import random

from src.constants.ascii_art import NUMBER_GUESS, CONGRATS
from src.constants.values import MIN, MAX, GUESSES


def choose_random_number():
    """ Select a random number between a range"""
    return random.randint(MIN, MAX)


def print_remaining_guesses(remaining_guesses):
    """ Print the remaining guesses left"""
    print(f"You have {remaining_guesses} attempts remaining to guess the number.")


def collect_guesses(difficulty: str, number: int) -> int:
    """ Collect the guesses of numbers"""
    number_of_guesses_remaining = GUESSES[difficulty]
    new_guess = 0
    previously_guessed = {}
    while number_of_guesses_remaining > 0 and new_guess != number:
        new_guess = int(input("Make a guess: "))
        if previously_guessed.get(new_guess) is not None:
            print(f"You have already guessed {new_guess}.")
        elif new_guess > number:
            print("Too high")
            number_of_guesses_remaining -= 1
            print_remaining_guesses(number_of_guesses_remaining)
        elif new_guess < number:
            print("Too low")
            number_of_guesses_remaining -= 1
            print_remaining_guesses(number_of_guesses_remaining)

        previously_guessed[new_guess] = True

    return new_guess


def print_result(guess: int, number: int):
    """ Display the result of the number guessing game"""
    if guess == number:
        print(f"{CONGRATS}")
        print(f"You guessed the number {number} correctly!")
    else:
        print(f"Better luck next time, the number was {number}")


def number_guessing():
    """ Number guessing game"""
    print(NUMBER_GUESS)
    difficulty = ""
    difficulty_exist = False
    while not difficulty_exist:
        difficulty = input(f"I\'m thinking of a number between {MIN} and {MAX}. "
                           f"Choose a difficulty \'easy\', \'medium\', \'hard\': ")
        if GUESSES.get(difficulty) is None:
            print(f"{difficulty} is not a difficulty option.")
        else:
            difficulty_exist = True

    number = choose_random_number()
    guess = collect_guesses(difficulty, number)
    print_result(guess, number)
