"""Test for Day 15 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.values import RESOURCES
from src.day_15 import coffee_maker
from src.constants.ascii_art import COFFEE


class Day15Test(unittest.TestCase):
    """Test for Day 15 of Coding"""
    def setUp(self):
        self.art = COFFEE.strip()
        self.out = StringIO()
        sys.stdout = self.out
        self.drink = ''
        self.change = ''
        self.error = ''
        self.resources = RESOURCES.items()

    def test_coffee_maker_espresso_with_change(self):
        """Test the Coffee Maker espresso with change"""
        # given
        self.drink = 'espresso'
        self.change = '$2.14'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\n10\n8\n6\n4\noff')):

            # when
            coffee_maker()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.change in actual)
            self.assertTrue(self.drink in actual)

    def test_coffee_maker_espresso_not_enough_money(self):
        """Test the Coffee Maker espresso with not enough money"""
        # given
        self.drink = 'espresso'
        self.error = 'Sorry, that\'s not enough money. Money refunded.'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\n0\n8\n6\n4\noff')):

            # when
            coffee_maker()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.error in actual)

    def test_coffee_maker_latte_with_no_change(self):
        """Test the Coffee Maker latte with no change"""
        # given
        self.drink = 'latte'
        self.change = '$0.00'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\n10\n0\n0\n0\noff')):

            # when
            coffee_maker()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.change in actual)
            self.assertTrue(self.drink in actual)

    def test_coffee_maker_cappuccino_with_change(self):
        """Test the Coffee Maker cappuccino with change"""
        # given
        self.drink = 'cappuccino'
        self.change = '$0.64'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\n10\n8\n6\n4\noff')):

            # when
            coffee_maker()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.change in actual)
            self.assertTrue(self.drink in actual)

    def test_coffee_maker_report(self):
        """Test the Coffee Maker report with no transactions"""
        # given
        self.resources = RESOURCES.items()
        with mock.patch('sys.stdin', new=StringIO('report\noff')):

            # when
            coffee_maker()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            for key, value in self.resources:
                self.assertTrue(key in actual)
                self.assertTrue(str(value) in actual)

    def test_coffee_maker_item_not_on_menu(self):
        # pylint: disable=R0801
        """Test the Coffee Maker with an item that is not on the meu"""
        # given
        self.drink = 'ice coffee'
        self.error = f'Sorry, {self.drink} is not in the menu'
        with mock.patch('sys.stdin', new=StringIO(f'{self.drink}\noff')):

            # when
            coffee_maker()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.error in actual)


if __name__ == '__main__':
    unittest.main()
