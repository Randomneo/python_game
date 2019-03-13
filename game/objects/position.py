from ..core.vector2 import Vector2


class Position(Vector2):

    @staticmethod
    def smooth_move(src_pos, dst_pos):
        delta_pos = dst_pos - src_pos
        delta_pos.mult_on_scalar(0.005)
        return src_pos + delta_pos

    def put_in_rect(self, x1, y1, x2, y2):
        if self.x < x1:
            self.x = x1
        if self.y < y1:
            self.y = y1
        if self.x > x2:
            self.x = x2
        if self.y > y2:
            self.y = y2

    def integering(self):
        self.x = int(self.x)
        self.y = int(self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Position(x=x, y=y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Position(x=x, y=y)
