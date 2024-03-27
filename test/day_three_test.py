""" Test for Day 3 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_three import treasure_island, TREASURE_IMAGE


class DayThreeTest(unittest.TestCase):
    """ Test cases for DAy 3 of Coding"""
    def test_treasure_image(self):
        """ Test the Treasure Island image"""
        # setup
        out = StringIO()

        with mock.patch('sys.stdin', new=StringIO("left\nswim")):
            # given
            expected = TREASURE_IMAGE.strip()
            sys.stdout = out

            # when
            treasure_island()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)



if __name__ == '__main__':
    unittest.main()
