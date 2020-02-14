import pygame
from enum import Enum
from Sound import Sound,Sounds

from GameObject import GameObject
from DuckHuntSprites import DogAnimationState

class Dog(GameObject):
    def __init__(self, display, stoper, spriteMap):
        positionVector = pygame.Vector2(50, 600-50)
        super().__init__(display, stoper, positionVector)
        self.gameDisplay = display
        self.dogState = DogState.SNIFFING
        self.spriteMap = spriteMap
        self.currentImageSet = self.spriteMap[DogAnimationState.SNIFF]
        self.duckAnimationState = DogAnimationState.SNIFF
        self.image = self.currentImageSet.getFrame()
        #Animation Stuff
        self.animationIntervalInMs = 100
        self.lastAnimationUpdate = 0
        self.finishedMovement = False
        # movement stuff
        self.movementSpeed = 2
        self.renderable = True
        self.start = True
        self.laughing_init = True
        self.hold_two_init = True
        self.timeStarted = 0

    def render(self):
        if self.renderable:
            self.gameDisplay.blit(self.image, self.positionVector)
        return None

    def tick(self):
        super().tick()
        if self.start:
            Sound.play(Sounds.DogSniff)
            self.start = False

        if self.dogState == DogState.SNIFFING:
            self.sniffing()
            return None

        if self.dogState == DogState.JUMPING:
            self.jumping()
            return None

        if self.dogState == DogState.HIDDEN:
            self.hidden()
            return None

        if self.dogState == DogState.HOLD_ONE:
            self.holdone()
            return None

        if self.dogState == DogState.HOLD_TWO:
            self.holdtwo()
            return None

        if self.dogState == DogState.LAUGHING:
            self.laughing()
            return None

    def sniffing(self):
        self.positionVector.x += self.movementSpeed
        if self.positionVector.x > 300:
            Sound.play(Sounds.SzczekTwo)
            self.dogState = DogState.JUMPING
            self.currentImageSet = self.spriteMap[DogAnimationState.JUMP]
        return None

    def jumping(self):
        self.positionVector.y -= 12
        self.positionVector.x += self.movementSpeed
        if self.positionVector.y < (600-200):
            self.dogState = DogState.HIDDEN
        return None

    def hidden(self):
        self.renderable = False
        self.finishedMovement = True
        return None

    def holdone(self):
        return None

    def holdtwo(self):
        if self.hold_two_init:
            self.timeStarted = self.stoper.getCurrentTicks()
            self.finishedMovement = False
            self.renderable = True
            self.positionVector.x = DogConsts.DOG_CENTER_X.value
            self.positionVector.y = DogConsts.DOG_CENTER_Y.value
            self.currentImageSet = self.spriteMap[DogAnimationState.HOLD_TWO]
            self.forceChangeAnimationFrame()
            self.hold_two_init = False
        if (self.stoper.getCurrentTicks()-self.timeStarted) > DogConsts.DOG_STATE_ON.value:
            self.hold_two_init = True
            self.dogState = DogState.HIDDEN
        return None

        return None

    def laughing(self):
        if self.laughing_init:
            self.timeStarted = self.stoper.getCurrentTicks()
            self.finishedMovement = False
            self.renderable = True
            self.positionVector.x = DogConsts.DOG_CENTER_X.value
            self.positionVector.y = DogConsts.DOG_CENTER_Y.value
            self.currentImageSet = self.spriteMap[DogAnimationState.LAUGHING]
            self.forceChangeAnimationFrame()
            self.laughing_init = False
        if (self.stoper.getCurrentTicks()-self.timeStarted) > DogConsts.DOG_STATE_ON.value:
            self.laughing_init = True
            self.dogState = DogState.HIDDEN
        return None

    def have_finished_movement(self):
        return self.finishedMovement


class DogState(Enum):
    SNIFFING = 0
    JUMPING = 1
    HIDDEN = 2
    HOLD_ONE = 3
    HOLD_TWO = 4
    LAUGHING = 5


class DogConsts(Enum):
    DOG_CENTER_X = 800 / 2 - 50
    DOG_CENTER_Y = 600 / 2 - 50
    DOG_STATE_ON = 2000
