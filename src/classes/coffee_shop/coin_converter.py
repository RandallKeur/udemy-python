""" Coin converter that is leveraged for the coffee maker."""


class CoinConverter:
    """ Models the coin converter"""

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """ Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """ Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin, value in self.COIN_VALUES.items():
            self.money_received += int(input(f"How many {coin}?: ")) * value
        return self.money_received

    def make_payment(self, cost):
        """ Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        print("Sorry that\'s not enough money. Money refunded.")
        self.money_received = 0
        return False
