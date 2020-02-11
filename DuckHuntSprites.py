from enum import Enum
import pygame

class DuckColor(Enum):
    BLUE = "blue"
    BLACK = "black"
    BROWN = "brown"

class DuckAnimationState(Enum):
    FALLING = "falling"
    HIT = "hit"
    HORIZONTAL = "horizontal"
    DIAGONAL = "diagonal"
    UP = "up"

class DogAnimationState(Enum):
    HOLD_ONE = "holdOne"
    HOLD_TWO = "holdTwo"
    JUMP = "jump"
    LAUGHING = "laughing"
    SNIFF = "sniff"    

class DuckDirection(Enum):
    RIGHT = "right",
    LEFT = "left"

MAX_DOG_ANIMATION_FRAMES = {
    DogAnimationState.HOLD_ONE : 1,
    DogAnimationState.HOLD_TWO : 1,
    DogAnimationState.JUMP : 3,
    DogAnimationState.LAUGHING : 2,
    DogAnimationState.SNIFF : 5
}

MAX_DUCK_ANIMATION_FRAMES = 3

class DuckSpriteSetRepository(object):
    def __init__(self):
        self.duckSpriteDictionary = self._prepareMap()

    def _prepareMap(self):
        duckSpriteDict = {}
        duckSpriteDict[DuckColor.BLUE] = self._prepareSpriteMapForColor(DuckColor.BLUE)
        duckSpriteDict[DuckColor.BLACK] = self._prepareSpriteMapForColor(DuckColor.BLACK)
        duckSpriteDict[DuckColor.BROWN] = self._prepareSpriteMapForColor(DuckColor.BROWN)
        return duckSpriteDict

    def _prepareOneFrameCollection(self, duckColor, duckAnimationSet):
        filePath = "images/" + duckColor.value + "_duck/" + duckAnimationSet.value + ".gif"
        collection = []
        collection.append(pygame.image.load(filePath).convert())
        return collection

    def _prepareAnimationCollection(self, duckColor, duckAnimationSet, imageCount):
        collection = []
        for i in range(1, imageCount + 1):
            filePath = "images/" + duckColor.value + "_duck/" + duckAnimationSet.value + "_" + str(i) + ".gif"
            collection.append(pygame.image.load(filePath).convert())
        return collection

    def _prepareSpriteMapForColor(self, duckColor):
        spriteMap = {}
        spriteMap[DuckAnimationState.FALLING] = self._prepareOneFrameCollection(duckColor, DuckAnimationState.FALLING)
        spriteMap[DuckAnimationState.HIT] = self._prepareOneFrameCollection(duckColor, DuckAnimationState.HIT)
        spriteMap[DuckAnimationState.HORIZONTAL] = self._prepareAnimationCollection(duckColor, DuckAnimationState.HORIZONTAL, 3)
        spriteMap[DuckAnimationState.DIAGONAL] = self._prepareAnimationCollection(duckColor, DuckAnimationState.HORIZONTAL, 3)
        spriteMap[DuckAnimationState.UP] = self._prepareAnimationCollection(duckColor, DuckAnimationState.HORIZONTAL, 3)
        return spriteMap

    def _prepareFourFrameAnimationFromThreeFrames(self, frames):
        return [frames[0],frames[1],frames[2],frames[1]]

    # TODO: make it blit images for
    def getCollectionForColor(self, duckColor):
        dict = self.duckSpriteDictionary[duckColor]
        return {
            DuckAnimationState.FALLING: RepeatingSpriteSet(dict[DuckAnimationState.FALLING]),
            DuckAnimationState.HIT: RepeatingSpriteSet(dict[DuckAnimationState.HIT]),
            DuckAnimationState.HORIZONTAL: RepeatingSpriteSet(self._prepareFourFrameAnimationFromThreeFrames(dict[DuckAnimationState.HORIZONTAL])),
            DuckAnimationState.DIAGONAL: RepeatingSpriteSet(self._prepareFourFrameAnimationFromThreeFrames(dict[DuckAnimationState.DIAGONAL])),
            DuckAnimationState.UP: RepeatingSpriteSet(self._prepareFourFrameAnimationFromThreeFrames(dict[DuckAnimationState.UP]))
        }

class DogSpriteSetRepository(object):
    def __init__(self):
        self.dogSpriteDictionary = self._prepareMap()

    def _prepareMap(self):
        dogSpriteDict = {}  
        for dogState in DogAnimationState:
            dogSpriteDict[dogState] = self._prepareAnimationCollection(dogState , MAX_DOG_ANIMATION_FRAMES[dogState] )
        return dogSpriteDict

    def _prepareAnimationCollection(self, dogAnimationSet, imageCount):
        collection = []
        for i in range(1, imageCount + 1):
            filePath = "images/dog/" + dogAnimationSet.value + "_" + str(i) + ".gif"
            collection.append(pygame.image.load(filePath).convert())
        return collection
    
    # TODO: make it blit images for
    def getCollection(self):
        dict = self.dogSpriteDictionary
        return {
            DogAnimationState.HOLD_ONE: RepeatingSpriteSet(dict[DogAnimationState.HOLD_ONE]),
            DogAnimationState.HOLD_TWO: RepeatingSpriteSet(dict[DogAnimationState.HOLD_TWO]),
            DogAnimationState.JUMP: RepeatingSpriteSet(dict[DogAnimationState.JUMP]),
            DogAnimationState.LAUGHING: RepeatingSpriteSet(dict[DogAnimationState.LAUGHING]),
            DogAnimationState.SNIFF: RepeatingSpriteSet(dict[DogAnimationState.SNIFF])
        }

class RepeatingSpriteSet(object):
    def __init__(self, frames):
        self.frames = frames
        self.currentFrameIndex = 0
        self.animationIncrement = 1
        self.maxFrames = len(frames) - 1

    def getFrame(self):
        return self.frames[self.currentFrameIndex]

    def nextFrame(self):
        self.currentFrameIndex += self.animationIncrement
        if self.currentFrameIndex == self.maxFrames or self.currentFrameIndex == 0:
            self.animationIncrement = -self.animationIncrement
