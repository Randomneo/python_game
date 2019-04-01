from pygame import Rect as pyRect
import pygame
from .. import screen_size, gravity
from .base import BaseGameObject
from .position import Position
from ..animation.animator import Animator
from ..animation.frames import FrameRow, Frame
from ..core.rect import Rect


walking_sprites = (
    20, 114,
    47, 68,
)


class Hero(BaseGameObject):
    speedx = 400
    speedy = 0
    on_gorund = False
    on_walk = False
    anim_jump = False

    def __init__(self, start_pos=Position(x=100, y=100)):
        super().__init__()
        self.size.x = 61
        self.size.y = 71
        self.is_animated = True
        self.is_hero = True
        self.pos = start_pos
        self.rect = pyRect(
            self.pos.x, self.pos.y,
            self.size.x, self.size.y
            )

    def load(self, rows_path, image_path):
        self.animator = Animator(image_path, size=self.size)
        self.animator.load(rows_path)
        frames_row = FrameRow()
        frames_row.speed = 1.0/10
        for i in range(8):
            frames_row.add(Frame(Rect(x=10 + 80*i, y=18, w=70 + 80*i, h=83)))
        self.animator.add_frames_row('stay', frames_row)
        self.animator.set_row('stay')

    def update_anim(self, time):
        self.animator.update_frame(time)
        self.animator.draw()

    @property
    def view_point(self):
        forward = 100
        if self.animator.flipx:
            forward *= -1

        return Position(
            x=self.pos.x + forward,
            y=self.pos.y - 50
        )

    def update_pos(self, keys, platforms, td):
        self.on_walk = False
        self.speedy += gravity
        if keys[pygame.K_SPACE] and self.on_gorund:
            self.speedy = -700
            self.current_frame = 0
            self.anim_jump = True
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.speedx * td
            self.animator.flipx = True
            self.on_walk = True
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.speedx * td
            self.animator.flipx = False
            self.on_walk = True
        self.pos.y += self.speedy * td

        self.on_gorund = False
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.x > screen_size[0] - self.rect.w:
            self.pos.x = screen_size[0] - self.rect.w
        if self.pos.y > screen_size[1] - self.rect.h:
            self.pos.y = screen_size[1] - self.rect.h
            self.speedy = 0
            self.on_gorund = True
            self.anim_jump = False

        self.rect.y = self.pos.y
        for item in platforms:
            if self.rect.colliderect(item.rect):
                if (self.speedy > 0):
                    self.rect.y = item.rect.y - self.rect.h
                    self.speedy = 0
                    self.on_gorund = True
                    self.anim_jump = False
                    self.pos.y = self.rect.y
                if (self.speedy < 0):
                    self.rect.y = item.rect.y + item.rect.h
                    self.speedy = 0
                    self.pos.y = self.rect.y

        self.rect.x = self.pos.x
        for item in platforms:
            if self.rect.colliderect(item.rect):
                if (keys[pygame.K_RIGHT]):
                    self.rect.x = item.rect.x - self.rect.w
                    self.pos.x = self.rect.x
                if (keys[pygame.K_LEFT]):
                    self.rect.x = item.rect.x + item.rect.w
                    self.pos.x = self.rect.x
