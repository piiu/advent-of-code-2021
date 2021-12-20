def solution(part1, part2=None):
    print('Part 1:', str(part1))
    print('Part 2:', str(part2))


def draw_map(map, placeholder='.'):
    min_y = min(map.point_map.keys())
    max_y = max(map.point_map.keys())

    min_x = max_x = None
    for x_row in map.point_map:
        min_in_row = min(map.point_map[x_row].keys())
        if not min_x or min_in_row < min_x:
            min_x = min_in_row

        max_in_row = max(map.point_map[x_row].keys())
        if not max_x or max_in_row > max_x:
            max_x = max_in_row

    for y in range(min_y, max_y + 1):
        line = ''
        for x in range(min_x, max_x + 1):
            existing_point = map.get_at(x, y)
            line += str(existing_point.value if existing_point else placeholder)
        print(line)
    print('')
