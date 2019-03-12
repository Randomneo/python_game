from pygame import Surface, SRCALPHA
from pygame import Rect
from pygame.image import load as load_img
from pygame.transform import flip
import pygame
from .. import screen_size, gravity
from .base import BaseGameObject
from .position import Position


walking_sprites = (
    20, 114,
    47, 68,
)


class Hero(BaseGameObject):
    size = (61, 70)
    image_path = 'game/res/hero_spritesheet.png'
    frames = {
        'stay': 8,
        'walk': 6,
        'jump': 2,
    }
    animation_speed = 1.0/10
    speedx = 400
    speedy = 0
    on_gorund = False
    flipx = False
    on_walk = False
    anim_jump = False
    pos = Position()

    def __init__(self, start_pos=Position(x=100, y=100)):
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

    def update_anim(self, time):
        self.last_frame_time += time
        if self.anim_jump:
            row = 297
            frames = self.frames['jump']
        elif self.on_walk:
            row = 110
            frames = self.frames['walk']
        else:
            row = 14
            frames = self.frames['stay']

        while self.last_frame_time > self.animation_speed:
            self.current_frame += 1
            self.last_frame_time = self.last_frame_time - self.animation_speed
        if not self.anim_jump:
            self.current_frame = self.current_frame % frames
        else:
            self.current_frame = min(self.current_frame, frames)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(
            self.spritesheet,
            (0, 0),
            (
                10 + (23 + 57)*self.current_frame,
                row,
                61, 70
            )
        )
        self.surface = flip(self.surface, self.flipx, False)

    def update_pos(self, keys, platforms, td):
        self.on_walk = False
        self.speedy += gravity
        if keys[pygame.K_SPACE] and self.on_gorund:
            self.speedy = -700
            self.current_frame = 0
            self.anim_jump = True
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.speedx * td
            self.flipx = True
            self.on_walk = True
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.speedx * td
            self.flipx = False
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

        self.rect.x = self.pos.x
        for item in platforms:
            if self.rect.colliderect(item.rect):
                if (keys[pygame.K_RIGHT]):
                    self.rect.x = item.rect.x - self.rect.w
                    self.pos.x = self.rect.x
                if (keys[pygame.K_LEFT]):
                    self.rect.x = item.rect.x + item.rect.w
                    self.pos.x = self.rect.x


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
