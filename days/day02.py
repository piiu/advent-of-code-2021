from utils import io

commands = io.get_input_rows()

depth = 0
position = 0
aim = 0  # aka depth dor part1

for command in commands:
    direction, distance = command.split(' ')
    distance = int(distance)
    if direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance
    elif direction == 'forward':
        position += distance
        depth += aim * distance

io.solution(aim * position, depth * position)
