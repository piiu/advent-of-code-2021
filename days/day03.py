from statistics import multimode
from utils import output, binary
from utils.input import Input

report = Input().rows_to_list()


def get_most_common_in_position(list_rows, position, fallback='1'):
    nth = [item[position] for item in list_rows]
    commons = multimode(nth)
    return commons[0] if len(commons) == 1 else fallback


g_rate = e_rate = ''
og_rate_candidates = cs_rate_candidates = report

for i in range(len(report[0])):
    most_common = get_most_common_in_position(report, i)
    least_common = binary.flip_bit(most_common)
    g_rate += most_common
    e_rate += least_common

    if len(og_rate_candidates) > 1:
        og_most_common = get_most_common_in_position(og_rate_candidates, i)
        og_rate_candidates = list(filter(lambda x: x[i] == og_most_common, og_rate_candidates))

    if len(cs_rate_candidates) > 1:
        cs_least_common = binary.flip_bit(get_most_common_in_position(cs_rate_candidates, i))
        cs_rate_candidates = list(filter(lambda x: x[i] == cs_least_common, cs_rate_candidates))


og_rate = ''.join(og_rate_candidates[0])
cs_rate = ''.join(cs_rate_candidates[0])

output.solution(binary.multiply(g_rate, e_rate), binary.multiply(og_rate, cs_rate))
