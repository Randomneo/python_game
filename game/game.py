import sys
import pygame
import time
from . import Colors, screen_size
from .objects.hero import Hero
from pygame import key

def start():
    pygame.init()

    screen = pygame.display.set_mode(screen_size)
    hero = Hero()

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
        hero.update_pos(keys)
        hero.update_anim(time_delta)

        screen.fill(Colors.black.value)
        hero.put_on_screen(screen)
        pygame.display.flip()
