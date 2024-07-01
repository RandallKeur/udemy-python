"""Test for Day 10 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_10 import calculator
from src.constants.values import CALCULATOR_OPERATIONS
from src.constants.ascii_art import CALCULATOR


class Day10Test(unittest.TestCase):
    """Test for Day 10 of Coding"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.art = CALCULATOR.strip()
        self.operations = CALCULATOR_OPERATIONS.strip()

    def test_calculator_multiplication(self):
        """Test the Calculator multiplication"""
        # given
        expected = "500"
        with mock.patch("sys.stdin", new=StringIO("100\n*\n5\nSTOP")):

            # when
            calculator()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.operations in actual)
            self.assertTrue(expected in actual)

    def test_calculator_division(self):
        """Test the Calculator division"""
        # given
        expected = "20"
        with mock.patch("sys.stdin", new=StringIO("100\n/\n5\nSTOP")):

            # when
            calculator()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.operations in actual)
            self.assertTrue(expected in actual)

    def test_calculator_subtraction(self):
        """Test the Calculator subtraction"""
        # given
        expected = "95"
        with mock.patch("sys.stdin", new=StringIO("100\n-\n5\nSTOP")):

            # when
            calculator()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.operations in actual)
            self.assertTrue(expected in actual)

    def test_calculator_addition(self):
        """Test the Calculator addition"""
        # given
        expected = "105"
        with mock.patch("sys.stdin", new=StringIO("100\n+\n5\nSTOP")):

            # when
            calculator()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.operations in actual)
            self.assertTrue(expected in actual)


if __name__ == "__main__":
    unittest.main()
