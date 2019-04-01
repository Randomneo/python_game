from pygame import Surface, SRCALPHA
from pygame.image import load as load_img
from pygame.transform import flip

from ..core.vector2 import Vector2
from ..core.rect import Rect
from ..animation.animation_types import AnimationType
from .frames import FrameRow, Frame


class Animator(object):

    def __init__(
            self,
            file_path,
            size=Vector2()):
        self.size = size
        self.file_path = file_path
        self.surface = Surface(self.size.get_t, SRCALPHA)

        self.spritesheet = load_img(file_path)
        self.surface.fill((0, 0, 0, 0))
        self.flipx = False
        self.frames_rows = {}
        self.current_frames_row = None

    def add_frames_row(self, name, frames_row):
        if isinstance(frames_row, FrameRow):
            self.frames_rows[name] = frames_row
        else:
            raise TypeError('Must be FrameRow type')

    def load(self, file):
        with open(file, 'r') as f:
            for entity in f.read().split('--')[1:]:
                obj = [t for t in entity.split('\n') if t and not t.isspace()]
                self.frames_rows[obj[0]] = FrameRow()
                if obj[1] == 'sycled':
                    self.frames_rows[obj[0]].animation_type = AnimationType.sycled
                elif obj[1] == 'stop':
                    self.frames_rows[obj[0]].animation_type = AnimationType.stop
                for row in obj[2:]:
                    x, y, w, h = row.split(', ')
                    self.frames_rows[obj[0]].add(
                        Frame(rect=Rect(x=x, y=y, w=w, h=h))
                    )

    def set_row(self, row):
        if row in self.frames_rows:
            self.current_frames_row = self.frames_rows[row]
            self.current_frames_row.current_frame = 0
            self.current_frames_row.last_frame_time = 0
        else:
            raise TypeError('Must be FrameRow type')

    def draw(self):
        self.surface.fill((0, 0, 0, 0))

        self.surface.blit(
            self.spritesheet,
            (0, 0),
            self.current_frames_row.frame
        )
        self.surface = flip(self.surface, self.flipx, False)

    def update_frame(self, time):
        self.current_frames_row.calculate_frame(time)
