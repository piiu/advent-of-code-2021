from utils.point import Point


class Map:
    def __init__(self):
        self.points = []
        self.point_map = {}
        self.mark = False

    def import_raw(self, raw):
        rows = raw.split('\n')
        for y, row in enumerate(rows):
            for x, value in enumerate(row.split()):
                self.add_point(Point(x, y, value))
        return self

    def get_at(self, x, y):
        if y in self.point_map and x in self.point_map[y]:
            return self.point_map[y][x]

    def get_by_value(self, value):
        return next((point for point in self.points if point.value == value), None)

    def add_point(self, point):
        self.points.append(point)
        if point.y in self.point_map:
            self.point_map[point.y][point.x] = point
        else:
            self.point_map[point.y] = {point.x: point}

