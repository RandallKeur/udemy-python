""" Test for Day 3 of Coding Challenges"""
import sys
import unittest
from io import StringIO
from unittest import mock

from src.ascii_art.art import ISLAND, ALLIGATOR, BOAT, FIRE, CARNIVOROUS_PLANTS, TREASURE
from src.day_three import treasure_island


class DayThreeTest(unittest.TestCase):
    """ Test cases for Day 3 of Coding"""

    def test_left_swim(self):
        """Test the Alligator image"""
        # setup
        out = StringIO()

        with mock.patch('sys.stdin', new=StringIO("left\nswim")):
            # given
            island = ISLAND.strip()
            alligator = ALLIGATOR.strip()
            sys.stdout = out

            # when
            treasure_island()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(island in actual, alligator in actual)

    def test_left_wait(self):
        """Test the Boat image"""
        # setup
        out = StringIO()

        with mock.patch('sys.stdin', new=StringIO("left\nwait\nblue")):
            # given
            island = ISLAND.strip()
            boat = BOAT.strip()
            sys.stdout = out

            # when
            treasure_island()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(island in actual, boat in actual)

    def test_right_red(self):
        """Test the Fire image"""
        # setup
        out = StringIO()

        with mock.patch('sys.stdin', new=StringIO("right\nred")):
            # given
            island = ISLAND.strip()
            fire = FIRE.strip()
            sys.stdout = out

            # when
            treasure_island()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(island in actual, fire in actual)

    def test_right_green(self):
        """Test the Plant image"""
        # setup
        out = StringIO()

        with mock.patch('sys.stdin', new=StringIO("right\ngreen")):
            # given
            island = ISLAND.strip()
            plants = CARNIVOROUS_PLANTS.strip()
            sys.stdout = out

            # when
            treasure_island()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(island in actual, plants in actual)

    def test_right_blue(self):
        """Test the Plant image"""
        # setup
        out = StringIO()

        with mock.patch('sys.stdin', new=StringIO("right\nblue")):
            # given
            island = ISLAND.strip()
            treasure = TREASURE.strip()
            sys.stdout = out

            # when
            treasure_island()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(island in actual, treasure in actual)


if __name__ == '__main__':
    unittest.main()
