"""Test for Day 15 of Coding Challenges"""
import os
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
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

    def test_coffee_machine_espresso_with_change(self):
        """Test the coffee machine espresso with change"""
        # setup
        drink = 'espresso'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\n10\n8\n6\n4\noff')):
            # given
            change = '$2.14'
            sys.stdout = self.out

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(change in actual)
            self.assertTrue(drink in actual)

    def test_coffee_machine_espresso_not_enough_money(self):
        """Test the coffee machine espresso with not enough money"""
        # setup
        drink = 'espresso'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\n0\n8\n6\n4\noff')):
            # given
            money_error = 'Sorry that\'s not enough money. Money refunded.'
            sys.stdout = self.out

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(money_error in actual)

    def test_coffee_machine_latte_with_no_change(self):
        """Test the coffee machine latte with no change"""
        # setup
        drink = 'latte'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\n10\n0\n0\n0\noff')):
            # given
            change = '$0.0'
            sys.stdout = self.out

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(change in actual)
            self.assertTrue(drink in actual)

    def test_coffee_machine_cappuccino_with_change(self):
        """Test the coffee machine cappuccino with change"""
        # setup
        drink = 'cappuccino'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\n10\n8\n6\n4\noff')):
            # given
            change = '$0.64'
            sys.stdout = self.out

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(change in actual)
            self.assertTrue(drink in actual)

    def test_coffee_machine_report(self):
        """Test the coffee machine report with no transactions"""

        with mock.patch('sys.stdin', new=StringIO('report\noff')):
            # given
            resources = self.coffee_maker.resources.items()
            sys.stdout = self.out

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            for key, value in resources:
                self.assertTrue(key in actual.lower())
                self.assertTrue(str(value) in actual)

    def test_coffee_machine_item_not_on_menu(self):
        """Test the coffee machine with an item that is not on the meu"""
        # setup
        drink = 'americano'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\noff')):
            # given
            menu_error = 'Sorry that item is not available.'
            sys.stdout = self.out

            # when
            coffee_machine(self.menu, self.coffee_maker, self.money_machine)
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(menu_error in actual)
