from utils import io

measurements = io.rows_to_int(io.get_input_rows())

count = 0
sliding_count = 0
for i, measurement in enumerate(measurements):
    if i == 0:
        continue
    count += measurement > measurements[i - 1]
    if i >= len(measurements) - 2:
        continue
    sliding_count += measurements[i + 2] > measurements[i - 1]

io.solution(count, sliding_count)
