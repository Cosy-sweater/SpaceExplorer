from dataclasses import dataclass


@dataclass
class SpaceshipData:
    small_weapon: tuple = ((8, 23), (47, 23))
    big_weapon: tuple = ((27, 30),)
