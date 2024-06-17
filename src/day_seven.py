"""Day 7 of Coding Challenges for Hangman"""
import random

from src.constants.ascii_art import CONGRATS, HANGMAN_LOGO, HANGMAN_STAGES


def init_dictionary():
    """Initialize the dictionary of words to choose from"""
    with open('src/shared_files/hangman_words.txt', 'r', encoding='utf-8') as file:
        dictionary = file.read().splitlines()
    return dictionary


def find_instances(word, letter):
    """Find all instances of a letter in a word"""
    return [i for i, character in enumerate(word) if character == letter]


def collect_guess(guessed_letters: list[str]):
    """Collect guess from input"""
    guessed_letter = input('Guess a letter: \n')
    while guessed_letter in guessed_letters:
        print(f'\nYou already guessed {guessed_letter}, try again\n')
        guessed_letter = input('Guess a letter: \n')
    return guessed_letter


def decide_win_or_lose(hangman_word: str, current_word: str):
    """Decide if they won or lost"""
    if hangman_word == current_word:
        print(CONGRATS)
        print('You won hangman\n')
    else:
        print('You are out of guesses, better luck next time\n'
              f'The word was {hangman_word}')


def replace_instances(indices: list[int], word: str, letter: str):
    """Puts letter in each index in indices"""
    for index in indices:
        word = word[:index] + letter + word[index + 1:]
    return word


def play_hangman():
    """Hangman game"""
    print(HANGMAN_LOGO)
    dictionary = init_dictionary()
    hangman_word = random.choice(dictionary)
    current_word = ''.join('_' for i in range(len(hangman_word)))
    letters_guessed = []
    remaining_guesses = len(HANGMAN_STAGES) - 1
    while hangman_word != current_word and remaining_guesses != 0:
        guessed_letter = collect_guess(letters_guessed)
        letters_guessed.append(guessed_letter)
        indices = find_instances(hangman_word, guessed_letter)
        if len(indices) != 0:
            print('Correct!\n')
            current_word = replace_instances(indices, current_word, guessed_letter)
        else:
            print('Incorrect guess. Try again.\n')
            remaining_guesses -= 1
        print(HANGMAN_STAGES[remaining_guesses])
        print(current_word)
    decide_win_or_lose(hangman_word, current_word)
