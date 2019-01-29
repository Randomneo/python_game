from pygame import Surface, SRCALPHA
from pygame import Rect
from pygame.image import load as load_img
from pygame.transform import flip
from .. import Colors
from .. import screen_size
import pygame


class Hero(object):
    size = (61, 70)
    image_path = 'game/res/hero_spritesheet.png'
    frames = 8
    animation_speed = 1.0/25
    speed = 0.2
    flipx = False
    pos = {'x': 0, 'y': 0}

    def __init__(self, start_pos=(100, 100)):
        self.surface = Surface(self.size, SRCALPHA)

        self.spritesheet = load_img(self.image_path)
        self.surface.fill((0, 0, 0, 0))
        self.pos['x'] = start_pos[0]
        self.pos['y'] = start_pos[1]
        self.rect = Rect(
            self.pos['x'], self.pos['y'],
            self.size[0], self.size[1]
            )
        self.current_frame = 0
        self.last_frame_time = 0

    def update_anim(self, time):
        self.last_frame_time += time
        while self.last_frame_time > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.frames
            self.last_frame_time = self.last_frame_time - self.animation_speed
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(
            self.spritesheet,
            (0, 0),
            (
                10 + (23 + 57)*self.current_frame,
                17,
                self.size[0],
                self.size[1]
            )
        )
        self.surface = flip(self.surface, self.flipx, False)
        

    def update_pos(self, keys):
        if keys[pygame.K_w]:
            self.pos['y'] -= self.speed
        if keys[pygame.K_a]:
            self.pos['x'] -= self.speed
            self.flipx = True
        if keys[pygame.K_s]:
            self.pos['y'] += self.speed
        if keys[pygame.K_d]:
            self.pos['x'] += self.speed
            self.flipx = False

        if self.pos['x'] < 0:
            self.pos['x'] = 0
        if self.pos['y'] < 0:
            self.pos['y'] = 0
        if self.pos['x'] > screen_size[0] - self.rect.w:
            self.pos['x'] = screen_size[0] - self.rect.w
        if self.pos['y'] > screen_size[1] - self.rect.h:
            self.pos['y'] = screen_size[1] - self.rect.h

        self.rect.x = self.pos['x']
        self.rect.y = self.pos['y']
        

    def put_on_screen(self, screen):
        screen.blit(self.surface, self.rect)
