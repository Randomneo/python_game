from .position import Position
from pygame import Rect as pyRect
from .base import BaseGameObject
from ..animation.animator import Animator
from ..animation.frames import FrameRow, Frame
from ..core.rect import Rect


class Platform(BaseGameObject):
    image_path = 'game/res/wall.png'
    pos = Position()

    def __init__(self, start_pos):
        super().__init__()
        self.is_interact_with_hero = True
        self.size.x = 50
        self.size.y = 20
        self.pos = start_pos
        self.rect = pyRect(
            self.pos.x, self.pos.y,
            self.size.x, self.size.y
            )
        self.animator = Animator(self.image_path, size=self.size)
        frames_row = FrameRow()
        frames_row.add(Frame(Rect(x=0, y=0, w=50, h=20)))
        self.animator.add_frames_row('stay', frames_row)
        self.animator.set_row('stay')
        self.animator.draw()
