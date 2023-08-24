from pathlib import Path
import pygame
pygame.font.init()

game_directory = str(Path.cwd())

base_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
cut_out_font = {i: pygame.font.Font(game_directory + "/assets/fonts/CutOutOFFont.otf", i) for i in range(10, 52)}


class Settings:
    def __init__(self):
        from json import load, dump
        self._json_load, self._json_dump = load, dump
        self._data = {}

        self.reload_settings()

    def reload_settings(self):
        with open(game_directory + "settings.json", "r") as f:
            self._data = self._json_load(f)

    def __getattr__(self, item):
        return self._data[item]


