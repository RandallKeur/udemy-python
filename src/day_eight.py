"""Day 8 of Coding Challenges for Caesar Cipher"""

from src.ascii_art.art import CAESAR_CIPHER


def shift(word: str, value: int):
    """Shifts each character in a word by a given value"""
    shifted_word = ''.join(chr(ord(char) + value) for char in word)
    print(shifted_word)


def caesar_cipher():
    """Caesar cipher"""
    print(CAESAR_CIPHER)
    running = True
    while running:
        decision = input("Type \"encode\" or \"decode:\"\n")
        word = input("Type your message:\n")
        shift_value = int(input("Type your shift number:\n"))
        if decision == "encode":
            shift(word, shift_value)
        elif decision == "decode":
            shift(word, -shift_value)
        else:
            print("Invalid\n")

        running = input("Do you want to continue?\n") == 'yes'
