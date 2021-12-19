import inspect
import re


class Input():
    def __init__(self):
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = module.__file__
        day = re.search('.*([0-9]{2})\.*py$', filename).groups()[0]
        self.raw = open('./../input/day' + day, 'r').read()
        self.rows = self.raw.split('\n')

    def rows_to_int(self):
        return [int(x) for x in self.rows]

    def rows_to_list(self):
        return [list(x) for x in self.rows]

    def rows_to_words(self):
        return [x.split() for x in self.rows]
