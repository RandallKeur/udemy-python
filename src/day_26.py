""" Day 26 of Coding Challenges for NATO Spelling"""

from src.classes.nato_converter import NatoConverter


def conversion():
    """ Convert a given string to NATO spelling"""
    converter = NatoConverter()
    is_on = True
    while is_on:
        converter.print_nato_code()
        is_on = converter.on()
