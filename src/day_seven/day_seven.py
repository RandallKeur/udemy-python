import random

from day_seven.hangman_art import stages, logo


class DaySeven:
    def __init__(self):
        self.dictionary = load_dictionary()
        print(logo)


def load_dictionary():
    file = open('src/day_seven/words.txt', 'r')
    dictionary = file.read().splitlines()
    file.close()
    return dictionary


def find_instances(word, letter):
    return [i for i, character in enumerate(word) if character == letter]


def hangman(self):
    hangman_word = random.choice(self.dictionary)
    current_word = "".join('_' for i in range(len(hangman_word)))
    guessed_letters = []
    guess_limit = len(stages) - 1
    while hangman_word != current_word and guess_limit != 0:
        guessed_letter = input("Guess a letter: \n")
        while guessed_letter in guessed_letters:
            print(f"\nYou already guessed {guessed_letter}, try again\n")
            guessed_letter = input("Guess a letter: \n")
        guessed_letters.append(guessed_letter)
        indices = find_instances(hangman_word, guessed_letter)
        if len(indices) != 0:
            print("Correct!\n")
            for index in indices:
                current_word = current_word[:index] + guessed_letter + current_word[index + 1:]
        else:
            print("Incorrect guess. Try again.\n")
            guess_limit -= 1
        print(stages[guess_limit])
        print(current_word)

    if hangman_word == current_word:
        print("Congratulations! You won hangman\n")
    else:
        print("You are out of guesses, better luck next time\n")
