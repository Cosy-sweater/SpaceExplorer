import game_object_template, global_data
import pygame

_screen = global_data.base_screen
clock = global_data.clock

pygame.font.init()
_font = global_data.cut_out_font[24]


class FPS(game_object_template.Object):
    def __init__(self, shown=True):
        self._is_shown = shown

    def show(self):
        self._is_shown = True

    def hide(self):
        self._is_shown = False

    def draw(self):
        surf = _font.render(str(int(clock.get_fps())), False, (0, 0, 0))
        _screen.blit(surf, (0, 0))
