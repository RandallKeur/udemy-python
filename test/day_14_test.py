"""Test for Day 14 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.day_14 import higher_lower
from src.constants.ascii_art import HIGHER_LOWER


class Day14Test(unittest.TestCase):
    """Test for Day 14 of Coding"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.art = HIGHER_LOWER.strip()

    def test_higher_lower_art(self):
        """Test the Higher or Lower image"""
        # given
        with mock.patch("sys.stdin", new=StringIO("A\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\nA\n"
                                                  "A\nA\nA\nA\nA\nA")):

            # when
            higher_lower()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)


if __name__ == "__main__":
    unittest.main()
