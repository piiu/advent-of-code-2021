from utils import output
from utils.input import Input

measurements = Input().rows_to_int()

count = sliding_count = 0

for i, measurement in enumerate(measurements):
    if i == 0:
        continue
    count += measurement > measurements[i - 1]
    if i >= len(measurements) - 2:
        continue
    sliding_count += measurements[i + 2] > measurements[i - 1]

output.solution(count, sliding_count)
