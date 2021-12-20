import inspect
import re
from utils.map import Map


class Input:
    def __init__(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        day = re.search('.*([0-9]{2})\.*py$', filename).groups()[0]
        self.raw = open('./../input/day' + day, 'r').read()
        self.rows = self.raw.splitlines()

    def rows_of_numbers(self):
        return [int(x) for x in self.rows]

    def rows_of_letters(self):
        return [list(x) for x in self.rows]

    def rows_of_words(self, separator=None):
        return [x.split(separator) for x in self.rows]

    def list_of_numbers(self, separator=','):
        return [int(x) for x in self.rows[0].split(separator)]

    def blocks_of_maps(self):
        return [Map().import_raw(x) for x in self.raw.split('\n\n')]

    def extract_first_row(self):
        first_row = self.rows[0]
        self.rows = self.rows[1:] if self.rows[1] else self.rows[2:]
        self.raw = '\n'.join(self.rows)
        return first_row
