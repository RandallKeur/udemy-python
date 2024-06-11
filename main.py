""" This main method runs the 100 days of coding challenges with interactive feedback"""
from src import day_five
from src import day_four
from src import day_one
from src import day_three
from src import day_two
from src import day_seven


def continue_running():
    """ Helper method to continue running the application based on feedback"""
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
                response = input("Invalid RESPONSE, please reply with \"yes\" or \"no\"\n")
    return None


def switchboard(day):
    """ Helper switchboard for routing feedback to each day's challenge"""
    decision_valid = False
    while not decision_valid:
        decision_valid = True
        match day:
            case "1":
                day_one.band_name_generator()
            case "2":
                day_two.calculate_tip()
            case "3":
                day_three.treasure_island()
            case "4":
                day_four.rock_paper_scissors()
            case "5":
                day_five.password_generator()
            case "6":
                print("Check out day_six.md file for more information")
            case "7":
                day_seven.play_hangman()
            case _:
                decision_valid = False
                day = input("Invalid input, please try again\n")


if __name__ == '__main__':
    STOP = False
    while not STOP:
        day_of_coding_challenge = input("Which day of coding challenge do you want to see?\n")
        switchboard(day_of_coding_challenge)
        STOP = continue_running()
