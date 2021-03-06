from enum import Enum
from .core.vector2 import Vector2

screen_size = width, height = 1040, 480
map_size = Vector2(x=10000, y=1000)
gravity = 1.5


class Colors(Enum):
    black = (0, 0, 0)
    white = (255, 255, 255)
