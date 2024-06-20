""" Test for Day 4 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_4 import map_text_to_art, Choices


class Day4Test(unittest.TestCase):
    """ Test for Day 1 of Coding"""

    def setUp(self):
        self.out = StringIO()
        self.selection = iter(['rock', 'paper', 'scissors', 'null'])
        self.expected = iter([Choices.rock, Choices.paper, Choices.scissors, Choices.invalid])

    def test_mappings(self):
        """ Test for mappings of rock, paper, scissors"""
        for var in self.selection:
            with mock.patch('sys.stdin', new=StringIO(var)):
                # given
                sys.stdout = self.out

                # when
                actual = map_text_to_art(var)

                # then
                self.assertEqual(actual, next(self.expected))


if __name__ == '__main__':
    unittest.main()
