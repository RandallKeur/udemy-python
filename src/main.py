# This is a sample Python script.
import day_one, day_two, day_three, day_four


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


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
                day_one.band_name_generator()
            case "2":
                day_two.tip_calculator()
            case "3":
                day_three.treasure_island()
            case "4":
                day_four.rock_paper_scissors()
            case _:
                decision_valid = False
                day = input("Invalid input, please try again\n")


if __name__ == '__main__':
    stop = False
    while not stop:
        day_of_coding_challenge = input("Which day of coding challenge do you want to see?\n")
        switchboard(day_of_coding_challenge)
        stop = continue_running()
