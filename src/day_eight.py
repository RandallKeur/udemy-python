"""Day 8 of Coding Challenges for Caesar Cipher"""
import string

from src.constants.ascii_art import CAESAR_CIPHER


def shift(plaintext: str, value: int):
    """Shifts each character in a word by a given value"""
    alphabet = string.ascii_letters
    value = value % len(alphabet)
    shifted_alphabet = alphabet[value:] + alphabet[:value]
    table = str.maketrans(alphabet, shifted_alphabet)
    print(plaintext.translate(table))


def caesar_cipher():
    """Caesar cipher"""
    print(CAESAR_CIPHER)
    running = True
    while running:
        decision = ''
        while decision not in ('encode','decode'):
            decision = input('Type \"encode\" or \"decode:\"\n')
        word = input('Type your message:\n')
        shift_value = int(input('Type your shift number:\n'))
        if decision == "encode":
            shift(word, shift_value)
        elif decision == "decode":
            shift(word, -shift_value)

        running = input('Do you want to continue?\n') == 'yes'
