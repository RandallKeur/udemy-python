""" Test for Day 8 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.ascii_art import CAESAR_CIPHER
from src.day_8 import caesar_cipher


class Day8Test(unittest.TestCase):
    """ Test cases for Day 8 of Coding"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.art = CAESAR_CIPHER.strip()
        self.inputs = {
            "encode_decode": "",
            "word": "",
            "shift": ""
        }
        self.expected = ""

    def test_caesar_cipher_swim_shift_3(self):
        """Test the Caesar Cipher with string and shift 3"""
        # given
        self.inputs["encode_decode"] = "encode"
        self.inputs["word"] = "swim"
        self.inputs["shift"] = "3"
        self.expected = "vzlp"
        with mock.patch("sys.stdin", new=StringIO(f"{self.inputs["encode_decode"]}\n"
                                                  f"{self.inputs["word"]}\n"
                                                  f"{self.inputs["shift"]}\n"
                                                  f"no\nno")):

            # when
            caesar_cipher()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.expected in actual)

    def test_caesar_cipher_spaces_symbols_shift_90(self):
        """Test the Caesar Cipher with string with spaces, symbols, numbers and a shift of 90"""
        # given
        self.inputs["encode_decode"] = "encode"
        self.inputs["word"] = "Testing_12345-!@#$% :)"
        self.inputs["shift"] = "90"
        self.expected = "FQefUZS_12345-!@#$% :)"
        with mock.patch("sys.stdin", new=StringIO(f"{self.inputs["encode_decode"]}\n"
                                                  f"{self.inputs["word"]}\n"
                                                  f"{self.inputs["shift"]}\n"
                                                  f"no\nno")):

            # when
            caesar_cipher()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            self.assertTrue(self.expected in actual)


if __name__ == "__main__":
    unittest.main()
