import sys
import pygame
import time
from . import Colors, screen_size
from .objects.hero import Hero
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

    cur_time = time.time()
    time_delta = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = key.get_pressed()

        time_delta = time.time()-cur_time
        cur_time = time.time()
        hero.update_pos(keys, platforms)
        hero.update_anim(time_delta)

        screen.fill(Colors.black.value)
        for item in to_draw:
            item.put_on_screen(screen)
        pygame.display.flip()
