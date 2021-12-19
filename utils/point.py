class Point:
    def __init__(self, x, y, value):
        self.x = int(x)
        self.y = int(y)
        self.value = value
        self.mark = False

    def equals(self, x, y):
        return self.x == x and self.y == y
