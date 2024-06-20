""" Day 16 of Coding Challenges for coffee machine using OOP"""
from src.day_16.menu import Menu
from src.day_16.coffee_maker import CoffeeMaker
from src.day_16.money_machine import MoneyMachine


def make_coffee():
    """Make a coffee for a customer"""
    print('Here is our menu:')
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    for item in menu.get_items():
        print(item)
    response = input('What would you like?: ')
    match response:
        case 'report':
            coffee_maker.report()
            money_machine.report()
        case 'off':
            return
        case _:
            drink = menu.find_drink(response)
    coffee_maker.is_resource_sufficient(drink)
    cost = money_machine.process_coins()
    money_machine.make_payment(cost)
    coffee_maker.make_coffee(drink)
