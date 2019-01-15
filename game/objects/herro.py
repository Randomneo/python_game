from pygame import Surface, SRCALPHA
from pygame import Rect
from pygame.image import load as load_img
from ..game import Colors

class Hero(object):
    size = (57, 80)
    image_path = 'game/res/hero_spritesheet.png'
    frames = 8
    animation_speed = 1.0/25

    def __init__(self, start_pos=(0, 0)):
        self.surface = Surface(self.size, SRCALPHA)

        self.spritesheet = load_img(self.image_path)
        self.surface.fill(Colors.black.value)
        self.rect = Rect()
        self.rect.move_ip(*start_pos)
        self.current_frame = 0
        self.last_frame_time = 0

    def update_anim(self, time):
        self.last_frame_time += time
        if self.last_frame_time > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.frames
        self.surface.fill(0, 0, 0, 0)
        self.surface.blit(
            self.spritesheet,
            (0, 0),
            (
                10 + (23 + 57)*self.current_frame, 17,
                17,
                self.size[0],
                self.size[1]
            )
        )

    def put_on_screen(self, screen):
        screen.blit(self.surface, self.surface.get_rect())
