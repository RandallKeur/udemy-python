""" Test for Day 3 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.constants.ascii_art import ISLAND, ALLIGATOR, BOAT, FIRE, CARNIVOROUS_PLANTS, TREASURE
from src.day_3 import treasure_island


class Day3Test(unittest.TestCase):
    """ Test cases for Day 3 of Coding"""
    def setUp(self):
        self.out = StringIO()
        sys.stdout = self.out
        self.art = []

    def test_left_swim(self):
        """Test the Alligator image"""
        # given
        self.art.extend([ISLAND.strip(), ALLIGATOR.strip()])
        with mock.patch("sys.stdin", new=StringIO("left\nswim")):

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            for art in self.art:
                self.assertTrue(art in actual)

    def test_left_wait(self):
        """Test the Boat image"""
        # given
        self.art.extend([ISLAND.strip(), BOAT.strip()])
        with mock.patch("sys.stdin", new=StringIO("left\nwait\nblue")):

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            for art in self.art:
                self.assertTrue(art in actual)

    def test_right_red(self):
        """Test the Fire image"""
        # given
        self.art.extend([ISLAND.strip(), FIRE.strip()])
        with mock.patch("sys.stdin", new=StringIO("right\nred")):

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            for art in self.art:
                self.assertTrue(art in actual)

    def test_right_green(self):
        """Test the Plant image"""
        # given
        self.art.extend([ISLAND.strip(), CARNIVOROUS_PLANTS.strip()])
        with mock.patch("sys.stdin", new=StringIO("right\ngreen")):

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            for art in self.art:
                self.assertTrue(art in actual)

    def test_right_blue(self):
        """Test the Treasure image"""
        # given
        self.art.extend([ISLAND.strip(), TREASURE.strip()])
        with mock.patch("sys.stdin", new=StringIO("right\nblue")):

            # when
            treasure_island()
            actual = self.out.getvalue().strip()

            # then
            for art in self.art:
                self.assertTrue(art in actual)


if __name__ == "__main__":
    unittest.main()
