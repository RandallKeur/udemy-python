""" Day 2 of Coding Challenges for Tip calculator"""


def calculate_tip():
    """ Calculate tip for given bill , people, and percentage"""
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill?: $"))
    people = int(input("How many people to split the bill?: "))
    tip_percent = int(input("What percentage tip would you like to give?: "))
    tip = round((total_bill * (1 + tip_percent / 100)) / people, 2)
    print(f"Each person should pay: ${tip}")
