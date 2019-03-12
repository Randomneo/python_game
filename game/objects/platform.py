from .position import Position
from pygame import Surface, SRCALPHA
from pygame import Rect
from pygame.image import load as load_img
from .base import BaseGameObject


class Platform(BaseGameObject):
    size = (50, 20)
    image_path = 'game/res/wall.png'
    pos = Position()

    def __init__(self, start_pos):
        super().__init__()
        self.surface = Surface(self.size, SRCALPHA)

        self.spritesheet = load_img(self.image_path)
        self.surface.fill((0, 0, 0, 0))
        self.pos = start_pos
        self.rect = Rect(
            self.pos.x, self.pos.y,
            self.size[0], self.size[1]
            )
        self.current_frame = 0
        self.last_frame_time = 0

        self.surface.blit(self.spritesheet, (0, 0))
