import pygame
from enum import IntEnum


class UIValues(IntEnum):
    SCORE = 0
    ROUND = 1
    DUCKS_IN_ROUND = 2
    DUCKS_FLEW = 3
    DUCKS_SHOT = 4
    AMMO = 5
    WAVE = 6
    WAVE_COUNT = 7


class UserInterface:

    def __init__(self, display):
        self.score = 0
        self.round = 0
        self.ducks_in_round = 0
        self.ducks_flew = 0
        self.ducks_shot = 0
        self.ammo = 0
        self.wave = 0
        self.wave_count = 0
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.display = display
        self.width, self.height = self.display.get_size()
        self.txt_color = pygame.Color('red')

    def set_txt_color(self, color):
        if isinstance(color, pygame.Color):
            TypeError("Must be pygame.Color, not %s" % type(color))
        self.txt_color = color

    def add_to_value(self, add, value):
        if not isinstance(value, UIValues):
            raise TypeError("Value to add must be UIValues type, not %s" % type(value))
        if not isinstance(add, int):
            raise TypeError("Score must be int type, not %s" % type(add))

        if value is UIValues.SCORE:
            self.score += add
            assert self.score >= 0
        elif value is UIValues.ROUND:
            self.round += add
            assert self.round >= 0
        elif value is UIValues.DUCKS_IN_ROUND:
            self.ducks_in_round += add
            assert self.ducks_in_round >= 0
        elif value is UIValues.DUCKS_FLEW:
            self.ducks_flew += add
            assert self.ducks_flew >= 0
        elif value is UIValues.DUCKS_SHOT:
            self.ducks_shot += add
            assert self.ducks_flew >= 0
        elif value is UIValues.AMMO:
            self.ammo += add
            assert self.ammo >= 0
        elif value is UIValues.WAVE:
            self.wave += add
            assert self.ammo >= 0
        elif value is UIValues.WAVE_COUNT:
            self.wave_count += add
            assert self.ammo >= 0

    def set_value(self, set_, value):
        if not isinstance(value, UIValues):
            raise TypeError("Value to add must be UIValues type, not %s" % type(value))
        if not isinstance(set_, int):
            raise TypeError("Score must be int type, not %s" % type(set_))

        if value is UIValues.SCORE:
            self.score = set_
            assert self.score >= 0
        elif value is UIValues.ROUND:
            self.round = set_
            assert self.round >= 0
        elif value is UIValues.DUCKS_IN_ROUND:
            self.ducks_in_round = set_
            assert self.ducks_in_round >= 0
        elif value is UIValues.DUCKS_FLEW:
            self.ducks_flew = set_
            assert self.ducks_flew >= 0
        elif value is UIValues.AMMO:
            self.ammo = set_
            assert self.ammo >= 0
        elif value is UIValues.WAVE:
            self.wave = set_
            assert self.ammo >= 0
        elif value is UIValues.WAVE_COUNT:
            self.wave = set_
            assert self.ammo >= 0

    def render_score(self):
        self.blit_txt('Score: %s' % self.score, (0, 0))

    def render_wave(self):
        self.blit_txt('Wave %s of %s' % (self.wave, self.wave_count), (120, 200))

    def render_round(self):
        self.blit_txt('Round: %s' % self.round, (200, 120))

    def blit_txt(self, txt, position):
        text = self.font.render(txt,
                                True,
                                self.txt_color)
        self.display.blit(text, position)

    def render_ui(self):
        self.render_score()
        self.render_wave()
        self.render_round()
