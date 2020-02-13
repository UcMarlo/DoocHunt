from enum import Enum

import pygame
from Crosshair import Crosshair
from Duck import Duck
from Stoper import Stoper
from DuckHuntSprites import DuckSpriteSetRepository, DuckColor, DogSpriteSetRepository
from Sound import Sound, Sounds
from UserInterface import UIValues, UserInterface


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
        self.gameState = GameState.ACTIVE_GAME


    # TODO: it looks awful, is there a good looking switch case?
    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print("mouse: ", mx, my)
            for duck in self.ducks:
                duck.checkIfShot(mx, my)
            self.sound.play(Sounds.GunShot)
            self.ui.add_to_value(-1, UIValues.AMMO)

    def main_loop(self):
        self.setup_round(1)
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

    def spawn_duck(self):
        for x in range(0, 20):
            self.ducks.append(Duck(
                self.display,
                self.stoper,
                pygame.Vector2(250, 250),
                self.duckSpriteRepository.getCollectionForColor(DuckColor.BROWN),
                self.ui))

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
        self.ui.add_to_value(5, UIValues.AMMO)
        self.spawn_duck()
        return None

# state impementations

    def game_starting(self):
        # Dog sniffing animation
        pass

    def round_starting(self):
        # Dog jumping animation
        pass

    def active_game(self):
        for duck in self.ducks:
            duck.tick()
        return None

    def round_end(self):
        # Dog laughing/happy animation
        pass

    def game_end(self):
        # game end and none is happy
        pass


class GameState(Enum):
    GAME_STARTING = 0
    ROUND_STARTING = 1
    ACTIVE_GAME = 2
    ROUND_END = 3
    GAME_END = 4
