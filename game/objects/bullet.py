from pygame import Rect
from pygame.image import load as load_img
from pygame.transform import flip
from pygame import Surface, SRCALPHA
from .position import Position


class Bullet(object):
    size = (10, 10)
    image_path = 'game/res/bullet.png'
    pos = Position()
    speed = 1

    def __init__(self, hero):
        self.surface = Surface(self.size, SRCALPHA)

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

    def update_pos(self):
        if self.direction:
            self.pos.x += self.speed
        else:
            self.pos.x -= self.speed

        self.rect.x = self.pos.x

    def put_on_screen(self, screen):
        print()
        screen.blit(self.surface, self.rect)
