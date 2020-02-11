import pygame
import math
from enum import Enum
from random import randint

from GameObject import GameObject
from DuckHuntSprites import DuckAnimationState

class Duck(GameObject):

    #TODO: make it use sprites instead of image
    def __init__(self, display, stoper, positionVector, spriteMap):
        super().__init__(display, stoper, positionVector)
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
        # movement speed
        self.movementSpeed = 0.1
        self.angle = 0
        self.setRandomAngle()


    def tick(self):
        super().tick()
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
        self.performTimeSynchronizedMove()
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

    def performTimeSynchronizedMove(self):
        self.positionVector.x += self.movementSpeed * self.stoper.getDetla() * self.directionVector.x
        self.positionVector.y += self.movementSpeed * self.stoper.getDetla() * self.directionVector.y

        return None

    def setRandomAngle(self):
        self.setDirectionFromAngle(randint(0, 360))

    def setDirectionFromAngle(self, angle):
        rads = math.radians(angle)
        x = math.cos(rads)
        y = math.sin(rads)
        self.directionVector = pygame.Vector2(x, y)

class DuckState(Enum):
    FLYING = 0
    DEAD = 1
    SHOT = 2
    ESCAPING = 3
    ESCAPED = 4
