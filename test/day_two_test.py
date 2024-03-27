""" Test for Day 2 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_two import calculate_tip


class MyTestCase(unittest.TestCase):
    """ Test for Day 2 of Coding"""
    def test_tip_calculator(self):
        """ Test for tip_calculator"""
        total_bill = 1000
        people = 10
        tip_percent = 20
        expected = '120'
        out = StringIO()
        with mock.patch('sys.stdin', StringIO(f"{total_bill}\n{people}\n{tip_percent}")):
            # given
            sys.stdout = out

            # when
            calculate_tip()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)


if __name__ == '__main__':
    unittest.main()
