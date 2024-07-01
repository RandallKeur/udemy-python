""" Test for Day 1 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import TestCase, mock
from src.day_1 import RESPONSE, band_name_generator


class Day1Test(TestCase):
    """ Test for Day 1 of Coding"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.inputs = {
            "cities": [],
            "pets": []
        }

    def test_band_name_generator(self):
        """ Test the Band Name Generator"""
        # given
        self.inputs["cities"] = ["city", "town", "Raleigh"]
        self.inputs["pets"] = ["pet", "barley", "Remi"]
        for city in self.inputs["cities"]:
            for pet in self.inputs["pets"]:
                expected = f"{RESPONSE} {city} {pet}"

                with mock.patch("sys.stdin", new=StringIO(f"{city}\n{pet}")):

                    # when
                    band_name_generator()
                    actual = self.out.getvalue().strip()

                    # then
                    self.assertTrue(expected in actual)


if __name__ == "__main__":
    unittest.main()
