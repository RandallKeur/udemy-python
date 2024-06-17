"""Day 12 of Coding Challenges for Number Guessing"""
import random

from src.constants.ascii_art import NUMBER_GUESS, CONGRATS
from src.constants.values import MIN, MAX, GUESSES


def choose_random_number():
    """Select a random number between a range"""
    return random.randint(MIN, MAX)


def print_remaining_guesses(remaining_guesses):
    """Print the remaining guesses left"""
    print(f'You have {remaining_guesses} attempts remaining to guess the number.')


def collect_guesses(difficulty: str, number: int) -> int:
    """Collect the guesses of numbers"""
    guesses = GUESSES[difficulty]
    guess = 0
    while guesses > 0 and guess != number:
        guess = int(input('Make a guess: '))
        if guess > number:
            print('Too high')
            guesses -= 1
            print_remaining_guesses(guesses)
        elif guess < number:
            print('Too low')
            guesses -= 1
            print_remaining_guesses(guesses)

    return guess


def print_result(guess: int, number: int):
    """Display the result of the number guessing game"""
    if guess == number:
        print(f'{CONGRATS}')
        print(f'You guessed the number {number} correctly!')
    else:
        print(f'Better luck next time, the number was {number}')


def number_guessing():
    """Number guessing game"""
    print(NUMBER_GUESS)
    difficulty = input(f'I\'m thinking of a number between {MIN} and {MAX}. '
                       f'Choose a difficulty \'easy\', \'medium\', \'hard\': ')
    number = choose_random_number()
    guess = collect_guesses(difficulty, number)
    print_result(guess, number)
