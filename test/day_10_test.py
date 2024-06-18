"""Test for Day 10 of Coding Challenges"""
import os
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_10 import calculator
from src.constants.values import CALCULATOR_OPERATIONS
from src.constants.ascii_art import CALCULATOR


class DayTenTest(unittest.TestCase):
    """Test for Day 10 of Coding"""

    def test_calculator_multiplication(self):
        """Test the Calculator multiplication"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO('100\n*\n5\nSTOP')):
            # given
            calculator_art = CALCULATOR.strip()
            operations = CALCULATOR_OPERATIONS.strip()
            expected = '500'
            sys.stdout = out

            # when
            calculator()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(calculator_art in actual, operations in actual)
            self.assertTrue(expected in actual)

    def test_calculator_division(self):
        """Test the Calculator division"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO('100\n/\n5\nSTOP')):
            # given
            calculator_art = CALCULATOR.strip()
            operations = CALCULATOR_OPERATIONS.strip()
            expected = '20'
            sys.stdout = out

            # when
            calculator()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(calculator_art in actual)
            self.assertTrue(operations in actual)
            self.assertTrue(expected in actual)

    def test_calculator_subtraction(self):
        """Test the Calculator subtraction"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO('100\n-\n5\nSTOP')):
            # given
            calculator_art = CALCULATOR.strip()
            operations = CALCULATOR_OPERATIONS.strip()
            expected = '95'
            sys.stdout = out

            # when
            calculator()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(calculator_art in actual)
            self.assertTrue(operations in actual)
            self.assertTrue(expected in actual)

    def test_calculator_addition(self):
        """Test the Calculator addition"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO('100\n+\n5\nSTOP')):
            # given
            calculator_art = CALCULATOR.strip()
            operations = CALCULATOR_OPERATIONS.strip()
            expected = '105'
            sys.stdout = out

            # when
            calculator()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(calculator_art in actual)
            self.assertTrue(operations in actual)
            self.assertTrue(expected in actual)
