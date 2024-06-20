"""Tests for Day 9 of the Coding Challenges"""
import os
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
        
    def test_silent_auction_tie(self):
        """Test the Silent Auction with a tie"""

        with mock.patch('sys.stdin', new=StringIO("jack\n100\nyes\njill\n100\nno")):
            # given
            auction = AUCTION.strip()
            gavel = GAVEL.strip()
            expected = 'tie'
            sys.stdout = self.out

            # when
            silent_auction()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(auction in actual, gavel in actual)
            self.assertTrue(expected in actual)

    def test_silent_auction_winner(self):
        """Test the Silent Auction with a winner"""

        with mock.patch('sys.stdin', new=StringIO('jack\n100\nyes\njill\n120\nno')):
            # given
            auction = AUCTION.strip()
            gavel = GAVEL.strip()
            expected = 'winner'
            sys.stdout = self.out

            # when
            silent_auction()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(auction in actual)
            self.assertTrue(gavel in actual)
            self.assertTrue(expected in actual)


if __name__ == '__main__':
    unittest.main()
