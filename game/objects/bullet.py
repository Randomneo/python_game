from pygame import Rect
from pygame.image import load as load_img
from pygame import Surface, SRCALPHA
from .position import Position
from .base import BaseGameObject
from .. import screen_size


class Bullet(BaseGameObject):
    size = (10, 10)
    image_path = 'game/res/bullet.png'
    speed = 700

    def __init__(self, hero):
        super().__init__()
        self.is_movable = True
        self.surface = Surface(self.size, SRCALPHA)
        self.pos = Position()

        self.direction = not hero.flipx
        self.pos.x = hero.pos.x
        self.pos.y = hero.pos.y + 20

        if self.direction:
            self.pos.x += hero.size[0]
        self.spritesheet = load_img(self.image_path)
        self.surface.fill((0, 0, 0, 0))
        self.rect = Rect(
            self.pos.x, self.pos.y,
            self.size[0], self.size[1]
            )
        self.current_frame = 0
        self.last_frame_time = 0
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(
            self.spritesheet,
            (0, 0),
            (0, 0, self.size[0], self.size[1])
        )

    def update_pos(self, time):
        if self.direction:
            self.pos.x += self.speed * time
        else:
            self.pos.x -= self.speed * time
        self.rect.x = self.pos.x

        if self.pos.x < 0 or self.pos.y < 0 or\
                self.pos.x > screen_size[0] - self.rect.w or \
                self.pos.y > screen_size[1] - self.rect.h:
            self.destroy()

    def put_on_screen(self, screen):
        screen.blit(self.surface, self.rect)
