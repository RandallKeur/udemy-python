"""Test for Day 15 of Coding Challenges"""
import os
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.values import RESOURCES
from src.day_15 import coffee_maker
from src.constants.ascii_art import COFFEE


class Day15Test(unittest.TestCase):
    """Test for Day 15 of Coding"""

    def test_coffee_maker_espresso_with_change(self):
        """Test the Coffee Maker espresso with change"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'
        drink = 'espresso'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\n10\n8\n6\n4\noff')):
            # given
            art = COFFEE.strip()
            change = '$2.14'
            sys.stdout = out

            # when
            coffee_maker()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
            self.assertTrue(change in actual)
            self.assertTrue(drink in actual)

    def test_coffee_maker_espresso_not_enough_money(self):
        """Test the Coffee Maker espresso with not enough money"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'
        drink = 'espresso'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\n0\n8\n6\n4\noff')):
            # given
            art = COFFEE.strip()
            money_error = 'Sorry, that\'s not enough money. Money refunded.'
            sys.stdout = out

            # when
            coffee_maker()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
            self.assertTrue(money_error in actual)

    def test_coffee_maker_latte_with_no_change(self):
        """Test the Coffee Maker latte with no change"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'
        drink = 'latte'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\n10\n0\n0\n0\noff')):
            # given
            art = COFFEE.strip()
            change = '$0.00'
            sys.stdout = out

            # when
            coffee_maker()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
            self.assertTrue(change in actual)
            self.assertTrue(drink in actual)

    def test_coffee_maker_cappuccino_with_change(self):
        """Test the Coffee Maker cappuccino with change"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'
        drink = 'cappuccino'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\n10\n8\n6\n4\noff')):
            # given
            art = COFFEE.strip()
            change = '$0.64'
            sys.stdout = out

            # when
            coffee_maker()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
            self.assertTrue(change in actual)
            self.assertTrue(drink in actual)

    def test_coffee_maker_report(self):
        """Test the Coffee Maker report with no transactions"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO('report\noff')):
            # given
            art = COFFEE.strip()
            resources = RESOURCES.items()
            sys.stdout = out

            # when
            coffee_maker()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
            for key, value in resources:
                self.assertTrue(key in actual)
                self.assertTrue(str(value) in actual)

    def test_coffee_maker_item_not_on_menu(self):
        """Test the Coffee Maker with an item that is not on the meu"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'
        drink = 'ice coffee'

        with mock.patch('sys.stdin', new=StringIO(f'{drink}\noff')):
            # given
            art = COFFEE.strip()
            menu_error = f'Sorry, {drink} is not in the menu'
            sys.stdout = out

            # when
            coffee_maker()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
            self.assertTrue(menu_error in actual)
