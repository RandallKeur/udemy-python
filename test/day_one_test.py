import sys
from io import StringIO
from unittest import TestCase, mock
from src.day_one import response, band_name_generator


class DayOneTest(TestCase):

    def get_input(self):
        return input(self)

    def test_band_name_generator(self):
        city = 'city'
        pet = 'pet'
        expected = f'{response} {city} {pet}'
        out = StringIO()
        with mock.patch('sys.stdin', StringIO("city\npet")):
            # given
            sys.stdout = out

            # when
            band_name_generator()
            actual = out.getvalue().strip()

            # then
            self.assertTrue(expected in actual)
