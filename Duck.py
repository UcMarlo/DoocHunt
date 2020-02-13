import pygame
import math
from enum import Enum
from random import randint
from Sound import Sound, Sounds

from GameObject import GameObject
from DuckHuntSprites import DuckAnimationState

class Duck(GameObject):

    #TODO: make it use sprites instead of image
    def __init__(self, display, stoper, positionVector, spriteMap, level):
        super().__init__(display, stoper, positionVector)
        self.gameDisplay = display
        self.duckState = DuckState.FLYING
        self.spriteMap = spriteMap
        self.currentImageSet = self.spriteMap[DuckAnimationState.HORIZONTAL]
        self.duckAnimationState = DuckAnimationState.HORIZONTAL
        # TODO: calculate it somehow
        self.imageCenterY = 16
        self.imageCenterX = 16
        self.image = self.currentImageSet.getFrame()
        #Animation Stuff
        self.animationIntervalInMs = 100
        self.lastAnimationUpdate = 0
        # movement stuff
        self.movementSpeed = 0.1 + (0.005 * (level - 1))
        self.angle = 0
        self.setRandomAngle()
        self.lastDirectionChange = 0
        self.flyingDirectionChangeThreshold = randint(1000, 5000)
        #Quacking
        self.quackingThreshold = randint(1000, 15000)
        self.lastQuacked = 0
        #State
        self.lastStateChanged = 0

    def render(self):
        if (self.renderable):
            horizontalFlip = self.directionVector.x < 0
            verticalFlip = self.directionVector.y > 0 and (self.duckAnimationState == DuckAnimationState.UP)
            self.gameDisplay.blit(pygame.transform.flip(self.image, horizontalFlip, verticalFlip), self.positionVector)
        return None

    def tick(self):
        super().tick()
        #TODO: create some "AI" logic

        #TODO: duck can "bounce" of the vertical walls of the screen. I think they might also bounce of, of the other ducks
        if self.duckState == DuckState.FLYING:
            self.flying()
            return None

        if self.duckState == DuckState.DEAD:
            self.dead()
            return None

        if self.duckState == DuckState.SHOT:
            self.shot()
            return None

        if self.duckState == DuckState.ESCAPING:
            self.escaping()
            return None

        if self.duckState == DuckState.ESCAPED:
            self.escaped()
            return None

        if self.duckState == DuckState.FALLING:
            self.falling()
            return None

        return None

    def flying(self):
        self.performTimeSynchronizedMove()
        self.checkForCollisionWithWall()
        # make duck flying pattern more random
        if self.stoper.getCurrentTicks() - self.lastDirectionChange > self.flyingDirectionChangeThreshold:
            self.setRandomAngle()
            self.lastDirectionChange = self.stoper.getCurrentTicks()
            self.flyingDirectionChangeThreshold = randint(1000, 5000)
        if self.stoper.getCurrentTicks() - self.lastQuacked > self.quackingThreshold:
            Sound.play(Sounds.Quack)
            self.quackingThreshold = randint(1000, 8000)
            self.lastQuacked = self.stoper.getCurrentTicks()

    def dead(self):
        return None

    def shot(self):
        if self.stoper.getCurrentTicks() - self.lastStateChanged > 500:
            self.duckState = DuckState.FALLING
            self.currentImageSet = self.spriteMap[DuckAnimationState.FALLING]
            self.setDirectionFromAngle(90)
            self.movementSpeed = 0.15
            Sound.play(Sounds.Falling)
        return None

    def escaping(self):
        self.performTimeSynchronizedMove()
        w,h = self.gameDisplay.get_size()

        if (self.positionVector.x - self.imageCenterX) < -self.imageCenterX*3 or (self.positionVector.x + self.imageCenterX) > w + (self.imageCenterX*3)\
                or (self.positionVector.y - self.imageCenterY) < -self.imageCenterY*3 or (self.positionVector.y + self.imageCenterY) > h + (self.imageCenterY*3):
            self.duckState = DuckState.ESCAPED
        # TODO: this is hardcoded and looks like p of s
            self.duckState = DuckState.ESCAPED
        return None

    def escaped(self):
        # Terminal status nothing to see here - removes tries
        return None

    def falling(self):
        self.performTimeSynchronizedMove()
        w, h = pygame.display.get_surface().get_size()
        if self.positionVector.y > h:
            self.duckState = DuckState.DEAD
            self.renderable = False
        return None

    def checkIfShot(self, x, y):
        if (self.duckState != DuckState.FLYING):
            return False

        spriteRect = self.image.get_rect().move(self.positionVector)
        if spriteRect.collidepoint(x, y):
            self.duckState = DuckState.SHOT
            self.lastStateChanged = self.stoper.getCurrentTicks()
            self.currentImageSet = self.spriteMap[DuckAnimationState.HIT]
            return True
        return False

    def performTimeSynchronizedMove(self):
        self.positionVector.x += self.movementSpeed * self.stoper.getDetla() * self.directionVector.x
        self.positionVector.y += self.movementSpeed * self.stoper.getDetla() * self.directionVector.y
        return None

    def checkForCollisionWithWall(self):
        w,h = self.gameDisplay.get_size()
        if (self.positionVector.x - self.imageCenterX) < 0 or (self.positionVector.x + self.imageCenterX) > w :
            self.directionVector.x = -self.directionVector.x
        # TODO: this is hardcoded and looks like p of s
        if (self.positionVector.y - self.imageCenterY) < 0 or (self.positionVector.y + self.imageCenterY) > h *0.8:
            self.directionVector.y = -self.directionVector.y

    def setRandomAngle(self):
        self.setDirectionFromAngle(randint(0, 360))

    def setDirectionFromAngle(self, angle):
        if self.duckState == DuckState.FLYING or self.duckState == DuckState.ESCAPING:
            if 80 <= angle <= 100 or 260 <= angle <= 280:
                self.currentImageSet = self.spriteMap[DuckAnimationState.UP]
                self.duckAnimationState = DuckAnimationState.UP
            if 0 <= angle <= 30 or 160 <= angle <= 210 or 330 <= angle <= 0:
                self.currentImageSet = self.spriteMap[DuckAnimationState.HORIZONTAL]
                self.duckAnimationState = DuckAnimationState.HORIZONTAL
            if 30 <= angle <= 80 or 110 <= angle <= 150 or 210 <= angle <= 250 or 270 <= angle <= 330:
                self.currentImageSet = self.spriteMap[DuckAnimationState.DIAGONAL]
                self.duckAnimationState = DuckAnimationState.DIAGONAL
        rads = math.radians(angle)
        x = math.cos(rads)
        y = math.sin(rads)
        self.directionVector = pygame.Vector2(x, y)
        return None

    def flyAway(self):
        self.duckState = DuckState.ESCAPING
        self.movementSpeed = 0.5
        self.setDirectionFromAngle(randint(250, 290))

class DuckState(Enum):
    FLYING = 0
    DEAD = 1
    SHOT = 2
    ESCAPING = 3
    ESCAPED = 4
    FALLING = 5
