"""Class to represent conversation between different formats"""
from pandas import read_csv

from src.constants.values import NATO_FILE


class NatoConverter:
    """Class to represent conversation between different formats"""

    def __init__(self):
        self.nato_dict = self.import_nato_csv_to_dictionary(NATO_FILE)

    @staticmethod
    def import_nato_csv_to_dictionary(filename: str) -> dict:
        """Method to import csv file to dictionary"""
        nato_data = read_csv(filename)
        return {row.letter: row.code for (index, row) in nato_data.iterrows()}

    def print_nato_code(self) -> None:
        """Method to get nato code from string"""
        result = []
        response = input("Please enter a word to spell out\n")
        for letter in response:
            result.append(self.nato_dict[letter.upper()])
        print(result)

    @staticmethod
    def on() -> bool:
        """Method to continue with conversions"""
        response = input("Do you want to convert more strings? (y/n): ")
        return response.strip() == 'y'
