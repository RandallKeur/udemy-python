""" Day 5 of Coding Challenges for Password Generator"""
from src.classes.password_generator import PasswordGenerator


def password_generator():
    """Password generator"""

    print("Welcome to the PyPassword Generator!")
    number_of_letters = input("How many letters would you like in your password?\n")
    number_of_symbols = input("How many symbols would you like?\n")
    number_of_numbers = input("How many numbers would you like?\n")
    generator = PasswordGenerator(number_of_letters, number_of_symbols, number_of_numbers)
    print(f"Here is your password: {generator.generate_password()}")
