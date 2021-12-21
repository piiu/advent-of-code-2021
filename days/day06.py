from utils import output
from utils.input import Input


def get_number_of_children(after_days, initial_offset):
    children = 0
    for day in range(initial_offset + 1, after_days + 1, 7):
        children += get_number_of_children(after_days, day + 8)
    return children + 1


def solve(after_days):
    timers = Input().list_of_numbers(',')
    return sum([get_number_of_children(after_days, x) for x in timers])


output.solution(solve(80), solve(256))
