"""Test for Day 11 of Coding Challenges"""
import os
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.values import STAND
from src.day_11 import blackjack
from src.constants.ascii_art import BLACKJACK


class Day11Test(unittest.TestCase):
    """Test for Day 11 of Coding"""

    def test_blackjack_stand(self):
        """Test the Blackjack stand"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO(f'{STAND}\nSTOP')):
            # given
            blackjack_art = BLACKJACK.strip()
            dealer = 'Dealer shows'

            sys.stdout = out

            # when
            blackjack()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(blackjack_art in actual)
            self.assertTrue(dealer in actual)
