"""Test for Day 12 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_12 import number_guessing
from src.constants.ascii_art import NUMBER_GUESS


class Day12Test(unittest.TestCase):
    """Test for Day 12 of Coding"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.art = NUMBER_GUESS.strip()
        self.inputs = {
            'number': 0,
            'error': '',
            'difficulty': ''
        }

    def test_number_guessing_art(self):
        """Test the Number Guessing image"""
        # given
        self.inputs['difficulty'] = 'easy'
        with mock.patch('sys.stdin', new=StringIO(f'{self.inputs['difficulty']}\n50\n25\n12\n6\n3\n2\n1')):

            # when
            number_guessing()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)

    def test_number_guessing_previously_guessed_number(self):
        """Test the Number Guessing game with a previously guessed number"""
        # given
        self.inputs['difficulty'] = 'easy'
        self.number = 50
        self.error = f'You have already guessed {self.number}.'
        with mock.patch('sys.stdin', new=StringIO(f'{self.inputs['difficulty']}\n{self.number}\n{self.number}\n25\n12'
                                                  f'\n6\n3\n2\n1')):

            # when
            number_guessing()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.error in actual)

    def test_number_guessing_with_invalid_difficulty(self):
        """Test the Number Guessing game with invalid difficulty selection"""
        # given
        wrong_difficulty = 'impossible'
        self.inputs['difficulty'] = 'easy'
        self.error = f'{wrong_difficulty} is not a difficulty option.'
        with mock.patch('sys.stdin', new=StringIO(f'{wrong_difficulty}\n{self.inputs['difficulty']}\n50\n25\n12\n6\n3\n2'
                                                  f'\n1')):

            # when
            number_guessing()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.error in actual)


if __name__ == '__main__':
    unittest.main()
