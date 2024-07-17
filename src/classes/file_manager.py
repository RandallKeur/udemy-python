""" Class to represent the file manager"""


class FileManager:
    """ Class to represent the file manager"""

    def __init__(self, read_file=None, write_file=None):
        self.read_file = read_file
        self.write_file = write_file

    def write_to_file(self, string_to_write: str):
        """ Method to write the information to file"""
        with open(self.write_file, 'a') as file:
            file.write(f"{string_to_write}\n")

