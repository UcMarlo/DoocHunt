import pygame
from enum import Enum


class Sounds(Enum):
    DogSniff = ['sounds/dog_sniff.wav', 0]
    Quack = ['sounds/quack.wav', 1]
    GunShot = ['sounds/gunshot.wav', 2]
    Loser = ['sounds/dog_sniff.wav', 3]
    Porazka = ['sounds/porazka.wav', 4]
    QuackReal = ['sounds/quack_real.wav', 5]
    Spadanie = ['sounds/spadanie.wav', 6]
    Szczek = ['sounds/szczek.wav', 7]
    SzczekTwo = ['sounds/szczek2.wav', 8]
    WallHit = ['sounds/wallhit.wav', 9]


class Sound:

    def __init__(self):
        pygame.mixer.init(44100, -16, 2, 2048)
        pygame.mixer.set_num_channels(len(Sounds.__members__))

    def play(self, sound, loops=0):
        """Play given sound, takes only Sounds enum as a parameter.

        :param Sounds sound: Sounds enumerator.
        :param int loops: how many times repeat the sound.

        """
        if not isinstance(sound, Sounds):
            raise TypeError("Must be Sounds Enum.")
        pygame.mixer.Channel(sound.value[1]).play(
            pygame.mixer.Sound(sound.value[0]))
