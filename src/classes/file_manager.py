""" Class to represent the file manager"""


class FileManager:
    """ Class to represent the file manager"""
    # pylint: disable=too-few-public-methods

    def __init__(self, read_file=None, write_file=None):
        self.read_file = read_file
        self.write_file = write_file

    def write_to_file(self, string_to_write: str):
        """ Method to write the information to file"""
        with open(self.write_file, 'a', encoding='utf-8') as file:
            file.write(f"{string_to_write}\n")
