from .objects.position import Position
from .core.vector2 import Vector2

from . import map_size, screen_size


class Camera(object):

    def __init__(self, screen, center_obj=None):
        self.pos = Position
        self.screen = screen
        self.screen_size = Vector2(screen_size[0], screen_size[1])
        self.map_maxs = map_size
        self.center_obj = center_obj

    def set_center_obj(self, obj):
        self.center_obj = obj

    def update_pos(self, center_on_hero=True):
        if self.center_obj:
            x = self.center_obj.pos.x - float(self.screen_size.x)/2
            y = self.center_obj.pos.y - float(self.screen_size.y)/2

        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x + self.screen_size.x > self.map_maxs.x:
            x = self.map_maxs.x - self.screen_size.x
        if y + self.screen_size.y > self.map_maxs.y:
            y = self.map_maxs.y - self.screen_size.y

        self.pos.x = x
        self.pos.y = y

    def draw(self, to_draw):
        for o in to_draw:
            self.screen.blit(
                o.surface,
                (
                    o.rect.x - self.pos.x,
                    o.rect.y - self.pos.y,
                )
            )
