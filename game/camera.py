from .objects.position import Position
from .core.vector2 import Vector2

from . import map_size, screen_size


class Camera(object):

    def __init__(self, hero, screen):
        self.pos = Position
        self.hero = hero
        self.screen = screen
        self.screen_size = Vector2(screen_size[0], screen_size[1])
        self.map_maxs = map_size
        self.to_draw = []

    def add_object_to_draw(self, object):
        if callable(object.put_on_screen):
            self.to_draw.append(object)
        else:
            raise TypeError('Object dont have put_on_screen method')

    def add_objects_to_draw(self, objects):
        if all(callable(t.put_on_screen) for t in objects):
            self.to_draw = [*self.to_draw, *objects]
        else:
            raise TypeError('Object dont have put_on_screen method')


    def update_pos(self, center_on_hero=True):
        if center_on_hero:
            x = self.hero.pos.x - float(self.screen_size.x)/2
            y = self.hero.pos.y - float(self.screen_size.y)/2

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

    def draw(self):
        for o in self.to_draw:
            self.screen.blit(
                o.surface,
                (
                    o.rect.x - self.pos.x,
                    o.rect.y - self.pos.y,
                )
            )