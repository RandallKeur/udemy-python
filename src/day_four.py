import random


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
