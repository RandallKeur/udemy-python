""" Test for Day 8 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.ascii_art.art import CAESAR_CIPHER
from src.day_eight import caesar_cipher


class DayThreeTest(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
