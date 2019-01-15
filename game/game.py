import sys
import pygame
import time
from . import Colors
from .objects.hero import Hero


def start():
    pygame.init()

    size = width, height = 640, 480

    screen = pygame.display.set_mode(size)
    hero = Hero()

    cur_time = time.time()
    time_delta = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        time_delta = time.time()-cur_time
        hero.update_anim(time_delta)
        cur_time = time.time()

        screen.fill(Colors.black.value)
        hero.put_on_screen(screen)
        pygame.display.flip()
