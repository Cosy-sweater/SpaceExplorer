import pygame
import global_data

size_multiplier = 2

# particles
glow_particle = pygame.image.load(global_data.game_directory + "/assets/particles/glow.png").convert_alpha()
glow_particle = pygame.transform.scale(glow_particle, (50, 50))


# player
player_base = (pygame.image.load(global_data.game_directory + "/assets/player/spaceship/base/spaceship_base001.png")
               .convert_alpha())
player_base = pygame.transform.scale_by(player_base, 2)