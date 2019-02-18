import sys
import pygame
import time
from . import Colors, screen_size
from .objects.hero import Hero
from .objects.bullet import Bullet
from .objects.platform import Platform
from .objects.position import Position
from pygame import key

def start():
    pygame.init()

    screen = pygame.display.set_mode(screen_size)
    hero = Hero()
    platforms = []
    for i in range(10):
        platforms.append(Platform(Position(x=0+i*50, y=300)))
    to_draw = [*platforms, hero]
    to_update_pos = []
    bullets = []

    cur_time = time.time()
    time_delta = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = key.get_pressed()
        if keys[pygame.K_a]:
            bullets.append(Bullet(hero))
            to_draw.append(bullets[-1])
            to_update_pos.append(bullets[-1])

        time_delta = time.time()-cur_time
        cur_time = time.time()
        for item in to_update_pos:
            item.update_pos()
        hero.update_pos(keys, platforms)
        hero.update_anim(time_delta)

        screen.fill(Colors.black.value)
        for item in to_draw:
            item.put_on_screen(screen)
        pygame.display.flip()
