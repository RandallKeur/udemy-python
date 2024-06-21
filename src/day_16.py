""" Day 16 of Coding Challenges for coffee machine using OOP"""
from src.classes.menu import Menu
from src.classes.coffee_maker import CoffeeMaker
from src.classes.money_machine import MoneyMachine

IS_ON = True


def make_drink(menu: Menu, coffee_maker: CoffeeMaker, money_machine: MoneyMachine, choice: str):
    """Make a drink for a customer"""
    drink = menu.find_drink(choice)
    if drink is not None:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


def coffee_machine(menu: Menu, coffee_maker: CoffeeMaker, money_machine: MoneyMachine):
    """Coffee machine for a customer to make a selection"""
    while IS_ON:
        options = menu.get_items()
        choice = input(f'What would you like?: ({options}): ')
        if choice == 'report':
            coffee_maker.report()
            money_machine.report()
        elif choice == 'off':
            return
        else:
            make_drink(menu, coffee_maker, money_machine, choice)
