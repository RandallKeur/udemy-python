""" Test for Day 1 of Coding Challenges"""
import sys
from io import StringIO
from unittest import TestCase, mock
from src.day_1 import RESPONSE, band_name_generator


class DayOneTest(TestCase):
    """ Test for Day 1 of Coding"""

    def test_band_name_generator(self):
        """ Test the band_name_generator"""
        city = iter(['city', 'town', 'Raleigh'])
        pet = iter(['pet', 'barley', 'Remi'])
        for i_city in city:
            # setup
            i_pet = next(pet)
            expected = f'{RESPONSE} {i_city} {i_pet}'
            out = StringIO()

            with mock.patch('sys.stdin', new=StringIO(f'{i_city}\n{i_pet}')):
                # given
                sys.stdout = out

                # when
                band_name_generator()
                actual = out.getvalue().strip()

                # then
                self.assertTrue(expected in actual)
