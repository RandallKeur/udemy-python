import random
import string


def generate_letters(length: int):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def generate_symbols(length: int):
    return ''.join(random.choice(string.punctuation) for _ in range(length))


def generate_numbers(length: int):
    return ''.join(random.choice(string.digits) for _ in range(length))


def randomize_string(letters: str, symbols: str, numbers: str):
    password = letters + symbols + numbers
    password = random.sample(password, len(password))
    return ''.join(password)


def password_generator():
    print("Welcome to the PyPassword Generator!")
    number_of_letters = input("How many letters would you like in your password?\n")
    number_of_symbols = input("How many symbols would you like?\n")
    number_of_numbers = input("How many numbers would you like?\n")
    letters = generate_letters(int(number_of_letters))
    symbols = generate_symbols(int(number_of_symbols))
    numbers = generate_numbers(int(number_of_numbers))
    print(f'Here is your password: {randomize_string(letters, symbols, numbers)}')
