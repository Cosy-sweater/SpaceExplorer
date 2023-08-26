from easing_functions import *
import pygame


class Camera:
    def __init__(self, easing=None):
        self.pos = [0, 0]
        self._easing_type = easing
        if self._easing_type is None:
            self._easing_type = LinearInOut

        self.following = None

    def move_to(self, pos, time=0):
        pass