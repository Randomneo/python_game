from pygame import Surface, SRCALPHA
from pygame import Rect
from pygame.image import load as load_img
from pygame.transform import flip
import pygame
from .. import Colors
from .. import screen_size, gravity
from .position import Position


class Hero(object):
    size = (61, 70)
    image_path = 'game/res/hero_spritesheet.png'
    frames = 8
    animation_speed = 1.0/25
    speedx = 0.2
    speedy = 0
    on_gorund = False
    flipx = False
    pos = Position()

    def __init__(self, start_pos=Position(x=100, y=100)):
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
                61, 70
            )
        )
        self.surface = flip(self.surface, self.flipx, False)
        

    def update_pos(self, keys, platforms):
        self.speedy += gravity
        if keys[pygame.K_w] and self.on_gorund:
            self.speedy = -0.5
        if keys[pygame.K_a]:
            self.pos.x -= self.speedx
            self.flipx = True
        if keys[pygame.K_d]:
            self.pos.x += self.speedx
            self.flipx = False
        self.pos.y += self.speedy

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

        self.rect.x = self.pos.x
        for item in platforms:
            if self.rect.colliderect(item.rect):
                if (keys[pygame.K_d]):
                    self.rect.x = item.rect.x - self.rect.w
                    self.pos.x = self.rect.x
                if (keys[pygame.K_a]):
                    self.rect.x = item.rect.x + item.rect.w
                    self.pos.x = self.rect.x


        self.rect.y = self.pos.y
        for item in platforms:           
            if self.rect.colliderect(item.rect):
                if (self.speedy > 0):
                    self.rect.y = item.rect.y - self.rect.h
                    self.speedy = 0
                    self.on_gorund = True
                    self.pos.y = self.rect.y
                if (self.speedy < 0):
                    self.rect.y = item.rect.y + item.rect.h
                    self.speedy = 0
                    self.pos.y = self.rect.y
                    
    def put_on_screen(self, screen):
        screen.blit(self.surface, self.rect)
