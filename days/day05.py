from utils import output
from utils.input import Input
from utils.map import Map
from utils.point import Point

lines = Input().rows_of_words(' -> ')
diagram = Map()
diagram_with_diagonals = Map()


def update_diagram(diagram, x, y):
    existing_point = diagram.get_at(x, y)
    if existing_point:
        existing_point.value += 1
    else:
        diagram.add_point(Point(x, y, 1))


for i, line in enumerate(lines):
    x1, y1 = [int(x) for x in line[0].split(',')]
    x2, y2 = [int(x) for x in line[1].split(',')]

    if x1 == x2 or y1 == y2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                update_diagram(diagram, x, y)
                update_diagram(diagram_with_diagonals, x, y)
    else:
        reverse = x2 < x1
        ascending = y2 < y1
        for offset in range(abs(x2-x1) + 1):
            x = x1 + offset * (-1 if reverse else 1)
            y = y1 + offset * (-1 if ascending else 1)
            update_diagram(diagram_with_diagonals, x, y)

# output.draw_map(diagram_with_diagonals)

overlaps = sum([1 if x.value > 1 else 0 for x in diagram.points])
overlaps_with_diagonals = sum([1 if x.value > 1 else 0 for x in diagram_with_diagonals.points])

output.solution(overlaps, overlaps_with_diagonals)
