class Vector2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def as_t(self):
        return (self.x, self.y)