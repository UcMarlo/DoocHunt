from enum import Enum

import pygame
from Crosshair import Crosshair
from Duck import Duck
from Stoper import Stoper
from DuckHuntSprites import DuckSpriteSetRepository, DuckColor
from Sound import Sound, Sounds

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
        self.run = True
        self.crosshair = Crosshair(self.display, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.ducks = []
        self.groundImage = pygame.image.load("images/ground.png")
        self.tree = pygame.image.load("images/tree.png")
        self.duckSpriteRepository = DuckSpriteSetRepository()

    # TODO: it looks awful, is there a good looking switch case?
    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print("mouse: ", mx, my)
            self.sound.play(Sounds.GunShot)

    def main_loop(self):
        self.setup_round(1)
        #TODO: prepare scene before main loop
        while self.run:
            self.stoper.newTick()
            self.crosshair.move(pygame.mouse.get_pos())

            for event in pygame.event.get():
                self.__handle_event(event)

            self.tick()
            self.render_and_display_frame()
        return None

    def render_and_display_frame(self):
        self.render_background()
        self.render_ducks()
        self.crosshair.render()
        pygame.display.update()

    def render_background(self):
        black = (80, 80, 130)  # TODO: background
        self.display.fill(black)

    def spawn_duck(self):
        for x in range(0, 20):
            self.ducks.append(Duck(self.display, self.stoper, pygame.Vector2(250, 250), self.duckSpriteRepository.getCollectionForColor(DuckColor.BROWN)))

    #TODO: theres a good place to setup a state machine - e.g. STARTING_TURN, TURN, WON_TURN, LOST_TURN etc.
    def tick(self):
        self.execute_ducks_logic()
        pass

    def execute_ducks_logic(self):
        for duck in self.ducks:
            duck.tick()

    def render_ducks(self):
        for duck in self.ducks:
            duck.render()

    def render_background(self):
        blue = (60, 80, 150) #TODO: background
        self.display.fill(blue)
        rect = self.groundImage.get_rect()
        self.display.blit(self.groundImage, (0, self.SCREEN_HEIGHT - rect.height ))
        return None

    class GameState(Enum):
        STARTING = 0
        ROUND_START = 1
        ACTIVE_GAME = 2
        ROUND_END = 3
        GAME_END = 4

    def setup_round(self, level):
        self.spawn_duck()
        return None
