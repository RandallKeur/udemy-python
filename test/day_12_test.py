"""Test for Day 12 of Coding Challenges"""
import os
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_12 import number_guessing
from src.constants.ascii_art import NUMBER_GUESS


class Day12Test(unittest.TestCase):
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

    def test_number_guessing_previously_guessed_number(self):
        """Test the Number Guessing game with a previously guessed number"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'
        duplicate = 50

        with mock.patch('sys.stdin', new=StringIO(f'easy\n{duplicate}\n{duplicate}\n25\n12\n6\n3\n2'
                                                  f'\n1')):
            # given
            art = NUMBER_GUESS.strip()
            duplicate_error = f'You have already guessed {duplicate}.'
            sys.stdout = out

            # when
            number_guessing()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
            self.assertTrue(duplicate_error in actual)

    def test_number_guessing_with_invalid_difficulty(self):
        """Test the Number Guessing game with invalid difficulty selection"""
        # setup
        out = StringIO()
        os.environ['TERM'] = 'xterm-256color'
        difficulty = 'impossible'

        with mock.patch('sys.stdin', new=StringIO(f'{difficulty}\neasy\n50\n25\n12\n6\n3\n2\n1')):
            # given
            art = NUMBER_GUESS.strip()
            difficulty_error = f'{difficulty} is not a difficulty option.'
            sys.stdout = out

            # when
            number_guessing()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(art in actual)
            self.assertTrue(difficulty_error in actual)
