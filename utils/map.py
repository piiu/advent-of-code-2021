from utils.point import Point


class Map:
    def __init__(self):
        self.points = []
        self.mark = False

    def import_raw(self, raw):
        rows = raw.split('\n')
        for y, row in enumerate(rows):
            for x, value in enumerate(row.split()):
                self.points.append(Point(x, y, value))
        return self

    def get_at(self, x, y):
        return next((point.value for point in self.points if point.x == x and point.y == y), None)

    def get_by_value(self, value):
        return next((point for point in self.points if point.value == value), None)
