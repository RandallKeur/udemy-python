"""Test for Day 11 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.values import STAND
from src.day_11 import blackjack
from src.constants.ascii_art import BLACKJACK


class Day11Test(unittest.TestCase):
    """ Test for Day 11 of Coding"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.art = BLACKJACK.strip()

    def test_blackjack_stand(self):
        # pylint: disable=R0801
        """ Test the Blackjack stand"""
        # given
        expected = "Dealer shows"
        with mock.patch("sys.stdin", new=StringIO(f"{STAND}\nSTOP")):

            # when
            blackjack()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(expected in actual)


if __name__ == "__main__":
    unittest.main()
