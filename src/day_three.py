""" Day 3 of Coding Challenges for Treasure Island"""


def island():
    """ Island portion of the game"""
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
    """ Crossroad left portion of the game"""
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
    """ Crossroad right portion of the game"""
    island()


def treasure_island():
    """ Treasure Island portion of the game"""
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
