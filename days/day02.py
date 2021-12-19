from utils import output
from utils.input import Input

commands = Input().rows_to_words()

depth = position = aim = 0

for command in commands:
    direction, distance = command
    distance = int(distance)
    if direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance
    elif direction == 'forward':
        position += distance
        depth += aim * distance

output.solution(aim * position, depth * position)
