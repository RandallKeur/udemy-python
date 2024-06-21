""" This main method runs the 100 days of coding challenges with interactive feedback"""
from src.constants.question_bank import QUESTION_BANK
from src.classes.quiz_generator import QuestionBank
from src.classes.coffee_maker import CoffeeMaker
from src.classes.menu import Menu
from src.classes.money_machine import MoneyMachine
from src.constants.ascii_art import GOODBYE
from src import (day_1, day_2, day_3, day_4, day_5, day_7, day_8, day_9,
                 day_10, day_11, day_12, day_13, day_14, day_15, day_16, day_17)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
question_bank = QuestionBank(QUESTION_BANK)


def continue_running():
    """ Helper method to continue running the application based on feedback"""
    response = input('\nWould you like to see another day\'s challenge?\n')
    decision_valid = False
    while not decision_valid:
        match response.lower():
            case 'yes':
                return False
            case 'no':
                print(f'{GOODBYE}\n'
                      'Thanks for playing!')
                return True
            case _:
                response = input('Invalid RESPONSE, please reply with \'yes\' or \'no\'\n')
    return None


def switchboard(day):
    """ Helper switchboard for routing feedback to each day's challenge"""
    decision_valid = False
    while not decision_valid:
        decision_valid = True
        match day:
            case '1':
                day_1.band_name_generator()
            case '2':
                day_2.calculate_tip()
            case '3':
                day_3.treasure_island()
            case '4':
                day_4.rock_paper_scissors()
            case '5':
                day_5.password_generator()
            case '6':
                print('Check out day_6.md file for more information')
            case '7':
                day_7.play_hangman()
            case '8':
                day_8.caesar_cipher()
            case '9':
                day_9.silent_auction()
            case '10':
                day_10.calculator()
            case '11':
                day_11.blackjack()
            case '12':
                day_12.number_guessing()
            case '13':
                day_13.run()
            case '14':
                day_14.higher_lower()
            case '15':
                day_15.coffee_maker()
            case '16':
                day_16.coffee_machine(menu, coffee_maker, money_machine)
            case '17':
                day_17.take_quiz(question_bank)
            case _:
                decision_valid = False
                day = input('Invalid input, please try again\n')


if __name__ == '__main__':
    STOP = False
    while not STOP:
        day_of_coding_challenge = input('Which day of coding challenge do you want to see?\n')
        switchboard(day_of_coding_challenge)
        STOP = continue_running()
