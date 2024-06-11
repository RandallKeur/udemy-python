import random

from ascii_art.art import hangman_stages, hangman_logo


class DaySeven:
    def __init__(self):
        self.dictionary = load_dictionary()
        print(hangman_logo)


def load_dictionary():
    file = open('src/shared_files/hangman_words.txt', 'r')
    dictionary = file.read().splitlines()
    file.close()
    return dictionary


def find_instances(word, letter):
    return [i for i, character in enumerate(word) if character == letter]


def collect_guess(guessed_letters: list[str]):
    guessed_letter = input("Guess a letter: \n")
    while guessed_letter in guessed_letters:
        print(f"\nYou already guessed {guessed_letter}, try again\n")
        guessed_letter = input("Guess a letter: \n")
    return guessed_letter


def decide_win_or_lose(hangman_word: str, current_word: str):
    if hangman_word == current_word:
        print("Congratulations! You won hangman\n")
    else:
        print(f"You are out of guesses, better luck next time\n"
              f"The word was {hangman_word}")


def replace_instances(indices: list[int], current_word: str, guessed_letter: str):
    for index in indices:
        current_word = current_word[:index] + guessed_letter + current_word[index + 1:]
    return current_word


def play_hangman(self):
    hangman_word = random.choice(self.dictionary)
    current_word = "".join('_' for i in range(len(hangman_word)))
    guessed_letters = []
    guess_limit = len(hangman_stages) - 1
    while hangman_word != current_word and guess_limit != 0:
        guessed_letter = collect_guess(guessed_letters)
        guessed_letters.append(guessed_letter)
        indices = find_instances(hangman_word, guessed_letter)
        if len(indices) != 0:
            print("Correct!\n")
            current_word = replace_instances(indices, current_word, guessed_letter)
        else:
            print("Incorrect guess. Try again.\n")
            guess_limit -= 1
        print(hangman_stages[guess_limit])
        print(current_word)
    decide_win_or_lose(hangman_word, current_word)
