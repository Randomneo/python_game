class Vector2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mult_on_scalar(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x=x, y=y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2(x=x, y=y)

    def __str__(self):
        return 'x={} y={}'.format(self.x, self.y)
