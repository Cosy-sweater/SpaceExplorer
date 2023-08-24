import sys
import pygame
from pygame.locals import *

import global_data
import gui.base
from visuals.particles import *
import assets

pygame.init()

fps = 90
clock = global_data.clock

screen = global_data.base_screen
width, height = screen.get_size()

HWND = pygame.display.get_wm_info()["window"]

game_objects = []

a = ParticleGenerator(vel_x_range=(-300, 300), vel_y_range=(-300, 300), gravity=0, acceleration=2, max_particles=2000,
                      generation_delay=0.001, pos=(width / 2, height / 2), sprites=(assets.glow_particle,),
                      lifetime_range=(2, 3))
game_objects.append(a)
game_objects.append(gui.base.FPS())

dt = 0
while True:
    screen.fill((128, 128, 128))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for i in game_objects:
        i.update(dt)

    for i in game_objects:
        i.draw()

    pygame.display.flip()
    dt = clock.tick(fps) / 1000
