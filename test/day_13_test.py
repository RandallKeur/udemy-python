"""Test for Day 13 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.ascii_art import DEBUGGING
from src.day_13 import run


class Day13Test(unittest.TestCase):
    """ Test for Day 13 of Coding"""

    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.art = DEBUGGING.strip()
        self.inputs = {
            "year": "",
            "age": "",
            "pages": "",
            "words_per_page": ""
        }

    def test_millennial_can_drive_multiple_pages(self):
        """ Test the Day 13 as a millennial who can drive and multiple pages"""
        # given
        self.inputs["year"] = "1990"
        self.inputs["age"] = "34"
        self.inputs["pages"] = "10"
        self.inputs["words_per_page"] = "225"
        expected = {"millennial": "You are a millennial.",
                    "drive": f"You can drive at age {self.inputs["age"]}.",
                    "words": "total words are: 2250",
                    "mutated_list": "mutated list result is: [2, 4, 6, 10, 16, 26]"}
        with mock.patch("sys.stdin", new=StringIO(f"{self.inputs["year"]}\n"
                                                  f"{self.inputs["age"]}\n"
                                                  f"{self.inputs["pages"]}\n"
                                                  f"{self.inputs["words_per_page"]}")):
            # when
            run()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            for value in expected.values():
                self.assertTrue(value in actual)

    def test_gen_z_cannot_drive_one_pages(self):
        """ Test the Day 13 as a Gen Z who cannot drive and one page"""
        # given
        self.inputs["year"] = "2012"
        self.inputs["age"] = "12"
        self.inputs["pages"] = "1"
        self.inputs["words_per_page"] = "210"
        expected = {"millennial": "You are a Gen Z.",
                    "drive": f"You cannot drive at age {self.inputs["age"]}.",
                    "words": "total words are: 210",
                    "mutated_list": "mutated list result is: [2, 4, 6, 10, 16, 26]"}
        with mock.patch("sys.stdin", new=StringIO(f"{self.inputs["year"]}\n"
                                                  f"{self.inputs["age"]}\n"
                                                  f"{self.inputs["pages"]}\n"
                                                  f"{self.inputs["words_per_page"]}")):
            # when
            run()
            actual = self.out.getvalue().strip()

            # then
            self.assertTrue(self.art in actual)
            for value in expected.values():
                self.assertTrue(value in actual)


if __name__ == "__main__":
    unittest.main()
