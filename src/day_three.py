""" Day 3 of Coding Challenges for Treasure Island"""
from src.ascii_art.art import TREASURE, ALLIGATOR, FIRE, CARNIVOROUS_PLANTS, BOAT, ISLAND

GAME_OVER = "Game Over!"


def island():
    """ Island portion of the game"""
    decision = input("You arrived at the island unharmed. There are 3 buildings. One is \"red\","
                     " one is \"green\" and one is \"blue\". Which one do you want to enter?\n")
    decision_valid = False
    while not decision_valid:
        match decision:
            case "red":
                decision_valid = True
                print("This building is full of fire, you burn alive."
                      f"{FIRE}"
                      f"{GAME_OVER}")
            case "green":
                decision_valid = True
                print("This building is full of plants... too bad they're carnivorous."
                      f"{CARNIVOROUS_PLANTS}"
                      f"{GAME_OVER}")
            case "blue":
                decision_valid = True
                print("This building is full of treasure... "
                      f"{TREASURE}"
                      "You Win!")
            case _:
                decision = input("Invalid choice, Please type \"red\", \"green\", or \"blue\"\n")


def crossroad_left():
    """ Crossroad left portion of the game"""
    decision = input("You arrived at a lake. There is an island in the middle of the lake. Do "
                     "you want to \"swim\" or \"wait\" for a boat?\n")
    decision_valid = False
    while not decision_valid:
        match decision:
            case "swim":
                decision_valid = True
                print("This lake is full alligators, you were eaten alive."
                      f"{ALLIGATOR}"
                      f"{GAME_OVER}")
            case "wait":
                decision_valid = True
                print(f"{BOAT}")
                island()
            case _:
                decision = input("Invalid choice, Please type \"swim\" or \"wait\"\n")


def crossroad_right():
    """ Crossroad right portion of the game"""
    island()


def treasure_island():
    """ Treasure Island portion of the game"""
    print(ISLAND)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    direction = input("You're at a crossroad. Where do you want to go? Type \"left\" "
                      "or \"right\"\n")
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
