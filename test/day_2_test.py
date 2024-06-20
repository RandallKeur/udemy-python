""" Test for Day 2 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_2 import calculate_tip


class Day2Test(unittest.TestCase):
    """ Test for Day 2 of Coding"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.inputs = {
            'bill': 0,
            'people': 0,
            'tip': 20
        }

    def test_tip_calculator(self):
        """ Test for Tip Calculator"""
        self.inputs['bill'] = 1000
        self.inputs['people'] = 10
        self.inputs['tip'] = 20
        self.expected = '120'
        with mock.patch('sys.stdin', StringIO(f'{self.inputs['bill']}\n'
                                              f'{self.inputs['people']}\n{self.inputs['tip']}')):

            # when
            calculate_tip()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.expected in actual)


if __name__ == '__main__':
    unittest.main()
