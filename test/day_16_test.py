"""Test for Day 16 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.classes.coffee_maker import CoffeeMaker
from src.classes.menu import Menu
from src.classes.money_machine import MoneyMachine
from src.day_16 import coffee_machine


class Day16Test(unittest.TestCase):
    """Test for Day 16 of Coding"""
    def setUp(self):
        # pylint: disable=R0801
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.out = StringIO()
        sys.stdout = self.out
        self.drink = ''
        self.change = ''
        self.error = ''

    def test_coffee_machine_espresso_with_change(self):
        """Test the coffee machine espresso with change"""
        # given
        self.drink = 'espresso'
        self.change = '$2.14'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\n'
                                                  f'10\n8\n6\n4\noff')):

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.drink in actual)
            self.assertTrue(self.change in actual)

    def test_coffee_machine_espresso_not_enough_money(self):
        """Test the coffee machine espresso with not enough money"""
        # given
        self.drink = 'espresso'
        self.error = 'Sorry that\'s not enough money. Money refunded.'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\n'
                                                  f'0\n8\n6\n4\noff')):

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.error in actual)

    def test_coffee_machine_latte_with_no_change(self):
        """Test the coffee machine latte with no change"""
        # given
        self.drink = 'latte'
        self.change = '$0.0'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\n'
                                                  f'10\n0\n0\n0\noff')):

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.drink in actual)
            self.assertTrue(self.change in actual)

    def test_coffee_machine_cappuccino_with_change(self):
        """Test the coffee machine cappuccino with change"""
        # given
        self.drink = 'cappuccino'
        self.change = '$0.64'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\n'
                                                  f'10\n8\n6\n4\noff')):

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.drink in actual)
            self.assertTrue(self.change in actual)

    def test_coffee_machine_report(self):
        """Test the coffee machine report with no transactions"""
        # given
        resources = self.coffee_maker.resources.items()
        with mock.patch('sys.stdin', new=StringIO('report\noff')):

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            for key, value in resources:
                self.assertTrue(key in actual.lower())
                self.assertTrue(str(value) in actual)

    def test_coffee_machine_item_not_on_menu(self):
        """Test the coffee machine with an item that is not on the meu"""
        # given
        self.drink = 'americano'
        self.error = 'Sorry that item is not available.'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\noff')):

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.error in actual)


if __name__ == '__main__':
    unittest.main()
