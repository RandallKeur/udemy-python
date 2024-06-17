""" Test for Day 8 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.ascii_art import CAESAR_CIPHER
from src.day_8 import caesar_cipher


class DayEightTest(unittest.TestCase):
    """ Test cases for Day 8 of Coding"""
    def test_caesar_cipher_swim_shift_3(self):
        """Test the Caesar Cipher image"""
        # setup
        out = StringIO()

        with mock.patch('sys.stdin', new=StringIO("encode\nswim\n3\nno\nno")):
            # given
            logo = CAESAR_CIPHER.strip()
            expected = 'vzlp'
            sys.stdout = out

            # when
            caesar_cipher()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(logo in actual, expected in actual)

    def test_caesar_cipher_spaces_symbols_shift_90(self):
        """Test the Caesar Cipher image"""
        # setup
        out = StringIO()

        with mock.patch('sys.stdin', new=StringIO('encode\nTesting_12345-!@#$% :)\n90\nno\nno')):
            # given
            logo = CAESAR_CIPHER.strip()
            expected = 'FQefUZS_12345-!@#$% :)'
            sys.stdout = out

            # when
            caesar_cipher()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(logo in actual, expected in actual)


if __name__ == '__main__':
    unittest.main()
