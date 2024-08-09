""" Coffee Shop"""
from src.classes.coffee_shop.coffee_maker import CoffeeMaker
from src.classes.coffee_shop.coin_converter import CoinConverter
from src.classes.coffee_shop.menu import Menu


class CoffeeShop:
    """ Models the coffee shop"""
    def __init__(self):
        self.coffee_maker = CoffeeMaker()
        self.menu = Menu()
        self.coin_converter = CoinConverter()
        self.open = True

    def process_order(self, order: str) -> None:
        """ Process the order from the customer"""
        drink = self.menu.find_drink(order)
        if drink is not None:
            if (self.coffee_maker.is_resource_sufficient(drink) and
                    self.coin_converter.make_payment(drink.cost)):
                self.coffee_maker.make_coffee(drink)

    def take_orders(self) -> None:
        """ Takes order from the customer"""
        while self.open:
            options = self.menu.get_items()
            order = input(f"What would you like?: ({options}): ")
            if order == "report":
                self.coffee_maker.report()
                self.coin_converter.report()
            elif order == "off":
                self.open = False
            else:
                self.process_order(order)
