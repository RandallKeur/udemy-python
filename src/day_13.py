"""Day 13 of Coding Challenges for Debugging"""
from random import randint

from src.constants.ascii_art import DEBUGGING


def you_got_it(limit: int):
    """Print "you got it" when you reach the limit"""
    for i in range(1, limit):
        if i == limit:
            print("You got it")


def dice():
    """Randomly generate where the dice lands"""
    dice_sides = ["❶", "❷", "❸", "❹", "❺", "❻"]
    dice_num = randint(0, len(dice_sides) - 1)
    print(f"dice landed on {dice_sides[dice_num]}")


def is_millennial():
    """Check whether the person is a millennial"""
    year = int(input("What\'s your year of birth?: "))
    if 1980 < year <= 1994:
        print("You are a millennial.")
    elif year > 1994:
        print("You are a Gen Z.")


def can_drive():
    """Check whether the person can drive"""
    age = int(input("How old are you?: "))
    if age >= 18:
        print(f"You can drive at age {age}.")
    else:
        print(f"You cannot drive at age {age}.")


def calculate_words():
    """Calculate the number of words in a paper"""
    pages = int(input("Number of pages: "))
    word_per_page = int(input("Number of words per page: "))
    total_words = pages * word_per_page
    print(f"total words are: {total_words}")


def mutate(a_list):
    """Mutate a list of numbers"""
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(f"mutated list result is: {b_list}")


def run():
    """Run the day 13 program"""
    print(DEBUGGING)
    you_got_it(20)
    dice()
    is_millennial()
    can_drive()
    calculate_words()
    mutate([1, 2, 3, 5, 8, 13])
