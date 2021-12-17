from utils import input

measurements = input.rows_to_int(input.get_input_rows())

count = 0
sliding_count = 0
for i, measurement in enumerate(measurements):
    if i == 0:
        continue
    count += measurement > measurements[i - 1]
    if i >= len(measurements) - 2:
        continue
    sliding_count += measurements[i + 2] > measurements[i - 1]

print('Part 1:', str(count))
print('Part 2:', str(sliding_count))
