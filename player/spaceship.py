import global_data
import game_object_template
import assets
import pygame

screen = global_data.base_screen
clock = global_data.clock


class Spaceship(game_object_template.Object):
    def __init__(self):
        from other.config import spaceship_commands
        self._commands = spaceship_commands
        self.base_sprite = assets.player_base
        self.base_rect = self.base_sprite.get_rect()
        self.mask = pygame.mask.from_surface(self.base_sprite)

    def update(self, dt, inputs) -> None:
        for command in inputs:
            if command[1:] in self._commands:
                self.base_rect.x += 50

    def draw(self) -> None:
        screen.blit(self.base_sprite, self.base_rect)