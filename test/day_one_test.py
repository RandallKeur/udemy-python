""" Test for Day 1 of Coding Challenges"""
import sys
from io import StringIO
from unittest import TestCase, mock
from src.day_one import RESPONSE, band_name_generator


class DayOneTest(TestCase):
    """ Test for Day 1 of Coding"""

    def test_band_name_generator(self):
        """ Test the band_name_generator"""
        city = 'city'
        pet = 'pet'
        expected = f'{RESPONSE} {city} {pet}'
        out = StringIO()
        with mock.patch('sys.stdin', StringIO("city\npet")):
            # given
            sys.stdout = out

            # when
            band_name_generator()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)
