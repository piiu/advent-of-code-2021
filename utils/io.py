import inspect
import re


def get_input_rows():
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = module.__file__
    day = re.search(".*([0-9]{2})\.*py$", filename).groups()[0]
    file = open('./../input/day' + day, 'r').read()
    return file.split('\n')


def rows_to_int(rows):
    return [int(x) for x in rows]


def solution(part1, part2):
    print('Part 1:', str(part1))
    print('Part 2:', str(part2))
