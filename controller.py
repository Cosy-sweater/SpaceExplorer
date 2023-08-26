import pygame


class Controller:
    def __init__(self, cfg: dict):
        self._config = cfg

    def handle_inputs(self, events):
        res = []
        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                for key in self._config.keys():
                    if self._config[key] == event.unicode:
                        if event.type == pygame.KEYDOWN:
                            prefix = "+"
                        else:
                            prefix = "-"
                        res.append(prefix + key)
        return res
