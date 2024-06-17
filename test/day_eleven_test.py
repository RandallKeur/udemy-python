"""Test for Day 11 of Coding Challenges"""
import os
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.values import STAND
from src.day_eleven import blackjack
from src.constants.ascii_art import BLACKJACK


class DayElevenTest(unittest.TestCase):
    """Test for Day 11 of Coding"""

    def test_blackjack_art(self):
        """Test the Blackjack image"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO(f"{STAND}\nSTOP")):
            # given
            blackjack_art = BLACKJACK.strip()
            sys.stdout = out

            # when
            blackjack()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(blackjack_art in actual)
