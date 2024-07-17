""" Class to represent the password generator"""
from random import choice, sample
from string import ascii_letters, punctuation, digits


class PasswordGenerator:
    """ Class to represent the password generator"""

    def __init__(self, letters="5", numbers="4", symbols="3"):
        self.password = None
        self.number = {
            "letters": int(letters),
            "numbers": int(numbers),
            "symbols": int(symbols)
        }

    def generate_password(self):
        """ Method to generate a random password"""
        self.password = self.generate_random_letters() + self.generate_random_symbols() + self.generate_random_numbers()
        self.password = sample(self.password, len(self.password))
        return "".join(self.password)

    def generate_random_letters(self):
        """ Generate random letters"""
        return "".join(choice(ascii_letters) for _ in range(self.number["letters"]))

    def generate_random_symbols(self):
        """ Generate random symbols"""
        return "".join(choice(punctuation) for _ in range(self.number["symbols"]))

    def generate_random_numbers(self):
        """ Generate random numbers"""
        return "".join(choice(digits) for _ in range(self.number["numbers"]))
