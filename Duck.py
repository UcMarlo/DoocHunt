import pygame
from enum import Enum

class Duck(object):

    #TODO: make it use sprites instead of image
    def __init__(self, display, startingX, startingY):
        self.gameDisplay = display
        self.position = (startingX, startingY)
        self.image = pygame.image.load("images/duck.jpg")
        #self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.imageCenterX = self.image.get_height() / 2
        self.imageCenterY = self.image.get_width() / 2
        self.duckState = DuckState.FLYING



    def move(self, pos):
        x,y = pos
        self.mousePosition = (x - self.imageCenterX), (y - self.imageCenterY)

    def tick(self):
        #TODO: create some "AI" logic

        #TODO: duck can "bounce" of the vertical walls of the screen. I think they might also bounce of, of the other ducks
        if self.duckState == DuckState.FLYING:
            self.flying()

        if self.duckState == DuckState.DEAD:
            self.dead()

        if self.duckState == DuckState.SHOT:
            self.shot()

        if self.duckState == DuckState.ESCAPING:
            self.escaping()

        if self.duckState == DuckState.ESCAPED:
            self.escaped()

        return None

    def flying(self):
        # TODO: duck should fly in random directions
        return None

    def dead(self):
        # Terminal status nothing to see here - grants points
        return None

    def shot(self):
        # TODO: duck falling animation - just after being hit
        return None

    def escaping(self):
        # TODO: escaping animation - just before changing to escaped
        return None

    def escaped(self):
        # Terminal status nothing to see here - removes tries
        return None

    def render(self):
        self.gameDisplay.blit(self.image, self.position)

    def check_for_colision(self):

        return None

class DuckState(Enum):
    FLYING = 0
    DEAD = 1
    SHOT = 2
    ESCAPING = 3
    ESCAPED = 4
