# This is a sample Python script.
import random


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def band_name_generator():
    print("Welcome to the Band Name Generator")
    city = input("What city did you grow up in?\n")
    pet_name = input("What is your pet's name?\n")
    print(f"Your band name is {city} {pet_name}")


def tip_calculator():
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill?: $"))
    people = int(input("How many people to split the bill?: "))
    tip_percent = int(input("What percentage tip would you like to give?: "))
    tip = round((total_bill * (1 + tip_percent / 100)) / people, 2)
    print(f"Each person should pay: ${tip}")


def island():
    decision = input("You arrived at the island unharmed. There are 3 buildings. One is \"red\","
                     " one is \"green\" and one is \"blue\". Which one do you want to enter?\n")
    decision_valid = False
    while not decision_valid:
        match decision:
            case "red":
                decision_valid = True
                print("This building is full of fire, you burn alive. Game Over!")
            case "green":
                decision_valid = True
                print("This building is full of plants... too bad they're carnivorous. Game Over!")
            case "blue":
                decision_valid = True
                print("This building is full of treasure... You Win!")
            case _:
                decision = input("Invalid choice, Please type \"red\", \"green\", or \"blue\"\n")


def crossroad_left():
    decision = input("You arrived at a lake. There is an island in the middle of the lake. Do "
                     "you want to \"swim\" or \"wait\" for a boat?\n")
    decision_valid = False
    while not decision_valid:
        match decision:
            case "swim":
                decision_valid = True
                print("This lake is full alligators, you were eaten alive. Game Over!")
            case "wait":
                decision_valid = True
                island()
            case _:
                decision = input("Invalid choice, Please type \"swim\" or \"wait\"\n")


def crossroad_right():
    island()


def treasure_island():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    direction = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n")
    decision_valid = False
    while not decision_valid:
        match direction:
            case "left":
                decision_valid = True
                crossroad_left()
            case "right":
                decision_valid = True
                crossroad_right()
            case _:
                direction = input("Invalid direction, please type \"left\" or \"right\"\n")


class Options:
    rock = '''
    ROCK
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    paper = '''
    PAPER
        _______
    ---'   ____)______
              ________)
              _________)
             _________)
    ---.____________)
    '''
    scissors = '''
    SCISSORS
        _______
    ---'   ____)______
              ________)
           ____________)
          (____)
    ---.__(___)
    '''


def map_text_to_art(text: str) -> str:
    match text:
        case "rock":
            return Options.rock
        case "paper":
            return Options.paper
        case "scissors":
            return Options.scissors
        case _:
            return "Invalid"


computer_win = "Computer Wins"
you_win = "You Win!"


def determine_winner(choice, computer):
    print("Computer chose: " + computer)
    if choice == computer:
        print("Draw")
    if choice == Options.rock:
        if computer == Options.scissors:
            print(you_win)
        if computer == Options.paper:
            print(computer_win)
    if choice == Options.scissors:
        if computer == Options.rock:
            print(computer_win)
        if computer == Options.paper:
            print(you_win)
    if choice == Options.paper:
        if computer == Options.rock:
            print(you_win)
        if computer == Options.scissors:
            print(computer_win)


def rock_paper_scissors():
    response = input("Welcome to Rock, Paper, Scissors... Which do you choose?\n")
    decision_valid = False
    computer_choice = random.choice([Options.rock, Options.paper, Options.scissors])
    while not decision_valid:
        choice = map_text_to_art(response.lower())
        decision_valid = True
        match choice:
            case Options.rock | Options.paper | Options.scissors:
                print("You chose: " + choice)
                determine_winner(choice, computer_choice)
            case _:
                decision_valid = False
                response = (input("Invalid response, please reply with \"rock\", \"paper\" or \"scissors\"\n")).lower()


def continue_running():
    response = input("\nWould you like to see another day's challenge?\n")
    decision_valid = False
    while not decision_valid:
        match response.lower():
            case "yes":
                return False
            case "no":
                print("Goodbye, thanks for playing!")
                return True
            case _:
                response = input("Invalid response, please reply with \"yes\" or \"no\"\n")


# Potential future idea --> Create enum for day challenge with brief description
# Use this in the switchboard and the welcome comment in each function
def switchboard(day):
    decision_valid = False
    while not decision_valid:
        decision_valid = True
        match day:
            case "1":
                band_name_generator()
            case "2":
                tip_calculator()
            case "3":
                treasure_island()
            case "4":
                rock_paper_scissors()
            case _:
                decision_valid = False
                day = input("Invalid input, please try again\n")


if __name__ == '__main__':
    stop = False
    while not stop:
        day_of_coding_challenge = input("Which day of coding challenge do you want to see?\n")
        switchboard(day_of_coding_challenge)
        stop = continue_running()
