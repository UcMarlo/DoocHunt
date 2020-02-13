import random
from enum import Enum

import pygame
from Crosshair import Crosshair
from Duck import Duck, DuckState
from Stoper import Stoper
from DuckHuntSprites import DuckSpriteSetRepository, DuckColor, DogSpriteSetRepository
from Sound import Sound, Sounds
from UserInterface import UIValues, UserInterface
from random import randint

class Game(object):

    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("DoocHunt")
        pygame.mouse.set_visible(False)
        self.stoper = Stoper()
        self.sound = Sound()
        self.ui = UserInterface(self.display)
        self.run = True
        self.crosshair = Crosshair(self.display, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.ducks = []
        self.groundImage = pygame.image.load("images/ground.png")
        self.tree = pygame.image.load("images/tree.png")
        self.duckSpriteRepository = DuckSpriteSetRepository()
        self.dogSpriteSetRepository = DogSpriteSetRepository()
        self.gameState = GameState.ROUND_STARTING
        self.level = 1
        self.ammoCount = self.level + 2
        self.duckCount = self.level + 1

    # TODO: it looks awful, is there a good looking switch case?
    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.gameState == GameState.ACTIVE_GAME:
                mx, my = pygame.mouse.get_pos()
                self.sound.play(Sounds.GunShot)
                self.ammoCount -= 1
                self.ui.set_value(self.ammoCount, UIValues.AMMO)
                for duck in self.ducks:
                    if duck.checkIfShot(mx, my):
                        self.ui.add_to_value(1, UIValues.DUCKS_SHOT)
                        self.ui.add_to_value(500*self.level, UIValues.SCORE)

    def main_loop(self):
        #TODO: prepare scene before main loop
        while self.run:
            self.stoper.newTick()
            self.crosshair.move(pygame.mouse.get_pos())
            if self.gameState == GameState.GAME_STARTING:
                self.game_starting()

            if self.gameState == GameState.ROUND_STARTING:
                self.round_starting()

            if self.gameState == GameState.ACTIVE_GAME:
                self.active_game()

            if self.gameState == GameState.ROUND_END:
                self.round_end()

            if self.gameState == GameState.GAME_END:
                self.game_end()

            self.render_and_display_frame()
            for event in pygame.event.get():
                self.__handle_event(event)
        return None

    def render_and_display_frame(self):
        self.render_background()
        self.render_ducks()
        self.render_bush()
        self.crosshair.render()
        self.ui.render_ui()
        pygame.display.update()

    def spawn_duck(self, level):
        color = random.choice(list(DuckColor))
        x = randint(self.SCREEN_WIDTH * 0.1, self.SCREEN_WIDTH * 0.9)
        y = randint(self.SCREEN_HEIGHT * 0.1, self.SCREEN_HEIGHT * 0.6)
        self.ducks.append(Duck(self.display, self.stoper, pygame.Vector2(x, y), self.duckSpriteRepository.getCollectionForColor(color), level))

    def render_ducks(self):
        for duck in self.ducks:
            duck.render()

    def render_background(self):
        blue = (60, 80, 150) #TODO: background
        self.display.fill(blue)
        return None

    def render_bush(self):
        rect = self.groundImage.get_rect()
        self.display.blit(self.groundImage, (0, self.SCREEN_HEIGHT - rect.height))

    def setup_round(self, level):
        self.ducks.clear()
        self.ammoCount = level + 2
        self.duckCount = level + 1
        self.ui.set_value(self.ammoCount, UIValues.AMMO)
        self.ui.set_value(0, UIValues.DUCKS_SHOT)
        self.ui.set_value(self.duckCount, UIValues.DUCKS_IN_ROUND)
        self.ui.set_value(self.level, UIValues.ROUND)
        for i in range(self.duckCount):
            self.spawn_duck(level)

        return None

# state impementations

    def game_starting(self):
        # Dog sniffing animation
        pass

    def round_starting(self):
        self.setup_round(self.level)
        self.gameState = GameState.ACTIVE_GAME
        pass

    def active_game(self):
        for duck in self.ducks:
            duck.tick()
        if (self.ammoCount == 0) or (self.ui.ducks_shot == self.ui.ducks_in_round):
            self.gameState = GameState.ROUND_END

        pass

    def round_end(self):
        # Dog laughing/happy animation
        for duck in self.ducks:
            if duck.duckState == DuckState.FLYING:
                duck.flyAway()
            duck.tick()

        if all(duck.duckState == DuckState.ESCAPED or duck.duckState == DuckState.DEAD for duck in self.ducks):
            self.gameState = GameState.ROUND_STARTING
            self.level += 1
        pass

    def game_end(self):
        assert False


class GameState(Enum):
    GAME_STARTING = 0
    ROUND_STARTING = 1
    ACTIVE_GAME = 2
    ROUND_END = 3
    GAME_END = 4
