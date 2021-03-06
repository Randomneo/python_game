import sys
import pygame
import time
from . import Colors, screen_size
from .objects.hero import Hero
from .objects.bullet import Bullet
from .objects.platform import Platform
from .objects.position import Position
from .camera import Camera
from .object_manager import ObjectManager
from .loader.load_map import LoadMap
from pygame import key


def start():
    pygame.init()
    obj_manager = ObjectManager()
    screen = pygame.display.set_mode(screen_size)

    level = LoadMap('./game/res/level.lvl')
    level.load(obj_manager)
    obj_manager.camera.screen = screen
    platforms = []
    for i in range(10):
        platforms.append(Platform(Position(x=0+i*50, y=300)))
    obj_manager.load_list(platforms)

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
            bullet = Bullet(obj_manager.hero)
            obj_manager.load_object(bullet)

        time_delta = time.time()-cur_time
        cur_time = time.time()
        for item in obj_manager.to_update_pos.objects:
            item.update_pos(time_delta)
        for item in obj_manager.to_update_anim.objects:
            item.update_anim(time_delta)
        obj_manager.hero.update_pos(keys, obj_manager.interact_with_hero.objects, time_delta)
        obj_manager.camera.update_pos()

        screen.fill(Colors.black.value)
        obj_manager.draw()
        pygame.display.flip()
