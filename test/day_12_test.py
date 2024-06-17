"""Test for Day 12 of Coding Challenges"""
import os
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_12 import number_guessing
from src.constants.ascii_art import NUMBER_GUESS


class DayTwelveTest(unittest.TestCase):
    """Test for Day 12 of Coding"""

    def test_number_guessing_art(self):
        """Test the Number Guessing image"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'

        with mock.patch('sys.stdin', new=StringIO('easy\n50\n25\n12\n6\n3\n2\n1')):
            # given
            art = NUMBER_GUESS.strip()
            sys.stdout = out

            # when
            number_guessing()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
