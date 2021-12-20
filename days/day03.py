from statistics import multimode
from utils import output
from utils.input import Input

report = Input().rows_of_letters()


def get_most_common_in_position(list_rows, position, fallback='1'):
    nth = [item[position] for item in list_rows]
    commons = multimode(nth)
    return commons[0] if len(commons) == 1 else fallback


def flip_bit(bit):
    return '1' if bit == '0' else '0'


g_rate = e_rate = ''
og_rate_candidates = cs_rate_candidates = report

for i in range(len(report[0])):
    most_common = get_most_common_in_position(report, i)
    g_rate += most_common
    e_rate += flip_bit(most_common)

    if len(og_rate_candidates) > 1:
        og_most_common = get_most_common_in_position(og_rate_candidates, i)
        og_rate_candidates = list(filter(lambda x: x[i] == og_most_common, og_rate_candidates))

    if len(cs_rate_candidates) > 1:
        cs_least_common = flip_bit(get_most_common_in_position(cs_rate_candidates, i))
        cs_rate_candidates = list(filter(lambda x: x[i] == cs_least_common, cs_rate_candidates))


og_rate = ''.join(og_rate_candidates[0])
cs_rate = ''.join(cs_rate_candidates[0])

output.solution(int(g_rate, 2) * int(e_rate, 2), int(og_rate, 2) * int(cs_rate, 2))
