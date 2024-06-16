"""Tests for Day 9 of the Coding Challenges"""
import os
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_nine import silent_auction
from src.constants.ascii_art import AUCTION, GAVEL


class DayNineTest(unittest.TestCase):
    """Tests for Day 9 of the Coding Challenges"""
    def test_silent_auction_tie(self):
        """Test the Caesar Cipher image"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO("jack\n100\nyes\njill\n100\nno")):
            # given
            auction = AUCTION.strip()
            gavel = GAVEL.strip()
            expected = 'tie'
            sys.stdout = out

            # when
            silent_auction()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(auction in actual, gavel in actual)
            self.assertTrue(expected in actual)

    def test_silent_auction_winner(self):
        """Test the Caesar Cipher image"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO("jack\n100\nyes\njill\n120\nno")):
            # given
            auction = AUCTION.strip()
            gavel = GAVEL.strip()
            expected = 'winner'
            sys.stdout = out

            # when
            silent_auction()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(auction in actual, gavel in actual)
            self.assertTrue(expected in actual)


if __name__ == '__main__':
    unittest.main()
