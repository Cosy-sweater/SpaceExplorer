import global_data
import game_object_template
import assets

screen = global_data.base_screen
clock = global_data.clock


class Spaceship(game_object_template.Object):
    def __init__(self):
        self.base_sprite = assets.player_base
        self.base_rect = self.base_sprite.get_rect()

    def update(self, dt) -> None:
        pass

    def draw(self) -> None:
        screen.blit(self.base_sprite, self.base_rect)