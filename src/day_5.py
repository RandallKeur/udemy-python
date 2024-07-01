""" Day 5 of Coding Challenges for Password Generator"""
import random
import string


def generate_random_letters(length: int):
    """Generate random letters"""
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def generate_random_symbols(length: int):
    """Generate random symbols"""
    return "".join(random.choice(string.punctuation) for _ in range(length))


def generate_random_numbers(length: int):
    """Generate random numbers"""
    return "".join(random.choice(string.digits) for _ in range(length))


def randomize_string(letters: str, symbols: str, numbers: str):
    """Randomize password"""
    password = letters + symbols + numbers
    password = random.sample(password, len(password))
    return "".join(password)


def password_generator():
    """Password generator"""
    print("Welcome to the PyPassword Generator!")
    number_of_letters = input("How many letters would you like in your password?\n")
    number_of_symbols = input("How many symbols would you like?\n")
    number_of_numbers = input("How many numbers would you like?\n")
    letters = generate_random_letters(int(number_of_letters))
    symbols = generate_random_symbols(int(number_of_symbols))
    numbers = generate_random_numbers(int(number_of_numbers))
    print(f"Here is your password: {randomize_string(letters, symbols, numbers)}")
