""" Test for Day 4 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_four import map_text_to_art, Choices


class DayFourTest(unittest.TestCase):
    """ Test for Day 1 of Coding"""
    def test_mappings(self):
        """ Test for mappings"""
        # setup
        selection = iter(['rock', 'paper', 'scissors', 'null'])
        expected = iter([Choices.rock, Choices.paper, Choices.scissors, Choices.invalid])

        for var in selection:
            # setup
            out = StringIO

            with mock.patch('sys.stdin', new=StringIO(var)):
                # given
                sys.stdout = out

                # when
                actual = map_text_to_art(var)

                # then
                self.assertEqual(actual, next(expected))


if __name__ == '__main__':
    unittest.main()
