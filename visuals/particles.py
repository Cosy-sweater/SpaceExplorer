import global_data, game_object_template
import pygame
from random import randint, uniform

screen = global_data.base_screen

base_particle = pygame.image.load(
    global_data.game_directory + "/assets/blank/particle.png").convert_alpha()


class Particle(game_object_template.Object):
    def __init__(self, x_vel=0, y_vel=0, pos=(0, 0), acceleration=0, gravity=0, lifetime=2, sprite=None):
        if x_vel == 0:
            x_vel = 0.01
            if randint(0, 1):
                x_vel *= -1
        if y_vel == 0:
            y_vel = 0.01
            if randint(0, 1):
                y_vel *= -1
        if acceleration == 0:
            acceleration = 0.00001
        if gravity == 0:
            gravity = 0.00001
        self.x_vel, self.y_vel = x_vel, y_vel
        self.gravity = gravity
        self.lifetime = lifetime
        self.x_acceleration = acceleration * self.x_vel / abs(self.x_vel)
        self.y_acceleration = acceleration * self.y_vel / abs(self.y_vel)
        self.x, self.y = pos

        if sprite is None:
            self.sprite = base_particle
        else:
            self.sprite = sprite
        self.rect = self.sprite.get_rect()

    def update(self, dt) -> None:
        self.x += self.x_vel * dt * 0.5
        self.y += self.y_vel * dt * 0.5
        self.x_vel += self.x_acceleration
        self.y_vel += self.y_acceleration + self.gravity
        self.x += self.x_vel * dt * 0.5
        self.y += self.y_vel * dt * 0.5

        self.lifetime -= dt
        if self.lifetime < 0:
            self.update = lambda *_: None

        self.rect.x, self.rect.y = self.x ,self.y

    def draw(self) -> None:
        screen.blit(self.sprite, self.rect)


class ParticleGenerator(game_object_template.Object):
    def __init__(self, vel_x_range=(0, 0), vel_y_range=(0, 0), acceleration=0, gravity=0, pos=(0, 0),
                 lifetime_range=(2, 2), max_particles=1, generation_delay=0.5, sprites=(None, None)):
        self.vel_x_range = vel_x_range
        self.vel_y_range = vel_y_range
        self.particle_acceleration = acceleration
        self.particle_gravity = gravity
        self.pos = pos
        self.particle_lifetime_range = lifetime_range

        self.max_particles = max_particles
        self.generation_delay = generation_delay

        self.sprites = sprites

        self._generation_timer = 0
        self._particles = []

    def update(self, dt) -> None:
        self._generation_timer += dt
        for particle in self._particles.copy():
            if particle.lifetime < 0:
                self._particles.remove(particle)

        if len(self._particles) < self.max_particles and self._generation_timer >= self.generation_delay:
            self._particles.append(
                Particle(
                    x_vel=randint(*self.vel_x_range),
                    y_vel=randint(*self.vel_y_range),
                    acceleration=self.particle_acceleration,
                    gravity=self.particle_gravity,
                    pos=self.pos,
                    sprite=self.rand_sprite(),
                    lifetime=uniform(*self.particle_lifetime_range)
                )
            )
            self._generation_timer %= self.generation_delay

        for particle in self._particles:
            particle.update(dt)

    def draw(self) -> None:
        for particle in self._particles:
            particle.draw()

    def rand_sprite(self):
        return self.sprites[randint(0, len(self.sprites) - 1)]
