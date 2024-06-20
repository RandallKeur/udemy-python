"""Tests for Day 9 of the Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_9 import silent_auction
from src.constants.ascii_art import AUCTION, GAVEL


class Day9Test(unittest.TestCase):
    """Tests for Day 9 of the Coding Challenges"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.art = [AUCTION.strip(), GAVEL.strip()]

    def test_silent_auction_tie(self):
        """Test the Silent Auction with a tie"""
        # given
        self.expected = 'tie'
        with mock.patch('sys.stdin', new=StringIO("jack\n100\nyes\njill\n100\nno")):

            # when
            silent_auction()
            actual = self.out.getvalue().strip()

            # then
            for art in self.art:
                self.assertTrue(art in actual)
            self.assertTrue(self.expected in actual)

    def test_silent_auction_winner(self):
        """Test the Silent Auction with a winner"""
        # given
        self.expected = 'winner'
        with mock.patch('sys.stdin', new=StringIO('jack\n100\nyes\njill\n120\nno')):

            # when
            silent_auction()
            actual = self.out.getvalue().strip()

            # then
            for art in self.art:
                self.assertTrue(art in actual)
            self.assertTrue(self.expected in actual)


if __name__ == '__main__':
    unittest.main()
