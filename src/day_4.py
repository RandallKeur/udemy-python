""" Day 4 of Coding Challenges for Rock, Paper, Scissors game"""

import random

from src.constants.ascii_art import ROCK, PAPER, SCISSORS


class Choices:
    # Disable too-few-public-methods error
    # pylint: disable=R0903
    """ Class to store constants for Rock, Paper, or Scissors"""
    rock = ROCK
    paper = PAPER
    scissors = SCISSORS
    invalid = "INVALID"


COMPUTER_WIN = "Computer Wins"
YOU_WIN = "You Win!"


def map_text_to_art(text: str) -> str:
    """ Map text to ASCII art for Rock, Paper, or Scissors"""
    match text:
        case "rock":
            return Choices.rock
        case "paper":
            return Choices.paper
        case "scissors":
            return Choices.scissors
        case _:
            return Choices.invalid


def determine_winner(choice, computer):
    """ Determine winner between user and computer"""
    print("Computer chose: " + computer)
    if choice == computer:
        print("Draw")
    if choice == Choices.rock:
        if computer == Choices.scissors:
            print(YOU_WIN)
        if computer == Choices.paper:
            print(COMPUTER_WIN)
    if choice == Choices.scissors:
        if computer == Choices.rock:
            print(COMPUTER_WIN)
        if computer == Choices.paper:
            print(YOU_WIN)
    if choice == Choices.paper:
        if computer == Choices.rock:
            print(YOU_WIN)
        if computer == Choices.scissors:
            print(COMPUTER_WIN)


def rock_paper_scissors():
    """ Play Rock, Paper, Scissors"""
    response = input("Welcome to Rock, Paper, Scissors... Which do you choose?\n")
    decision_valid = False
    computer_choice = random.choice([Choices.rock, Choices.paper, Choices.scissors])
    while not decision_valid:
        choice = map_text_to_art(response.lower())
        decision_valid = True
        match choice:
            case Choices.rock | Choices.paper | Choices.scissors:
                print("You chose: " + choice)
                determine_winner(choice, computer_choice)
            case _:
                decision_valid = False
                response = (input("Invalid RESPONSE, please reply with \'rock\', "
                                  "\'paper\' or \'scissors\'\n")).lower()
