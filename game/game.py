import sys
import pygame
import time
from . import Colors, screen_size, map_size
from .objects.hero import Hero
from .objects.bullet import Bullet
from .objects.platform import Platform
from .objects.position import Position
from .camera import Camera
from pygame import key


def start():
    pygame.init()

    screen = pygame.display.set_mode(screen_size)
    hero = Hero()
    camera = Camera(hero, screen)
    camera.add_object_to_draw(hero)
    platforms = []
    for i in range(10):
        platforms.append(Platform(Position(x=0+i*50, y=300)))
    camera.add_objects_to_draw(platforms)
    to_update_pos = []
    bullets = []

    cur_time = time.time()
    time_delta = 0
    last_frame_time = 0
    to_shoot = True
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = key.get_pressed()
        last_frame_time += time_delta
        while last_frame_time > 1:
            to_shoot = True
            last_frame_time = 0
        if keys[pygame.K_a] and to_shoot:
            to_shoot = False
            bullet = Bullet(hero)
            bullets.append(bullet)
            camera.add_object_to_draw(bullet)
            to_update_pos.append(bullet)

        time_delta = time.time()-cur_time
        cur_time = time.time()
        for item in to_update_pos:
            item.update_pos(time_delta)
        hero.update_pos(keys, platforms, time_delta)
        hero.update_anim(time_delta)
        camera.update_pos()

        screen.fill(Colors.black.value)
        camera.draw()
        pygame.display.flip()
