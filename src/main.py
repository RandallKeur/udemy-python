""" This main method runs the 100 days of coding challenges with interactive feedback"""
import day_five
import day_four
import day_one
import day_three
import day_two


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
            case _:
                decision_valid = False
                day = input("Invalid input, please try again\n")


if __name__ == '__main__':
    STOP = False
    while not STOP:
        day_of_coding_challenge = input("Which day of coding challenge do you want to see?\n")
        switchboard(day_of_coding_challenge)
        STOP = continue_running()
