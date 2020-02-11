import pygame
from enum import Enum

from GameObject import GameObject
from DuckHuntSprites import DuckAnimationState

class Duck(GameObject):

    #TODO: make it use sprites instead of image
    def __init__(self, display, stoper, position, spriteMap):
        super().__init__(display, stoper, position, None)
        self.gameDisplay = display
        self.duckState = DuckState.FLYING
        self.spriteMap = spriteMap
        self.currentImageSet = self.spriteMap[DuckAnimationState.HORIZONTAL]
        self.imageCenterY = 16 #self.image.get_width() / 2 TODO: calcualte it somehow
        self.imageCenterX = 16 #self.image.get_height() / 2
        self.image = self.currentImageSet.getFrame()
        #Animation Stuff
        self.animationIntervalInMs = 100
        self.lastAnimationUpdate = 0


    def move(self, pos):
        x,y = pos
        self.mousePosition = (x - self.imageCenterX), (y - self.imageCenterY)

    def _changeAnimationFrame(self):
        if self.stoper.getCurrentTicks() - self.lastAnimationUpdate > self.animationIntervalInMs:
            self.currentImageSet.nextFrame()
            self.lastAnimationUpdate = self.stoper.getCurrentTicks()
            self.image = self.currentImageSet.getFrame()


    def tick(self):
        self._changeAnimationFrame()
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

    def check_for_colision(self):

        return None

class DuckState(Enum):
    FLYING = 0
    DEAD = 1
    SHOT = 2
    ESCAPING = 3
    ESCAPED = 4
