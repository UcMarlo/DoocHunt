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

class DuckDirection(Enum):
    RIGHT = "right",
    LEFT = "left"

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
        spriteMap[DuckAnimationState.DIAGONAL] = self._prepareAnimationCollection(duckColor, DuckAnimationState.DIAGONAL, 3)
        spriteMap[DuckAnimationState.UP] = self._prepareAnimationCollection(duckColor, DuckAnimationState.UP, 3)
        return spriteMap

    def _prepareFourFrameAnimationFromThreeFrames(self, frames):
        return [frames[0],frames[1],frames[2],frames[1]]

    def getCollectionForColor(self, duckColor):
        dict = self.duckSpriteDictionary[duckColor]
        return {
            DuckAnimationState.FALLING: RepeatingSpriteSet(dict[DuckAnimationState.FALLING]),
            DuckAnimationState.HIT: RepeatingSpriteSet(dict[DuckAnimationState.HIT]),
            DuckAnimationState.HORIZONTAL: RepeatingSpriteSet(self._prepareFourFrameAnimationFromThreeFrames(dict[DuckAnimationState.HORIZONTAL])),
            DuckAnimationState.DIAGONAL: RepeatingSpriteSet(self._prepareFourFrameAnimationFromThreeFrames(dict[DuckAnimationState.DIAGONAL])),
            DuckAnimationState.UP: RepeatingSpriteSet(self._prepareFourFrameAnimationFromThreeFrames(dict[DuckAnimationState.UP]))
        }

class RepeatingSpriteSet(object):
    def __init__(self, frames):
        self.frames = frames
        self.currentFrameIndex = 0
        self.maxFrames = len(frames) - 1

    def getFrame(self):
        return self.frames[self.currentFrameIndex]

    def nextFrame(self):
        if self.currentFrameIndex == self.maxFrames:
            self.currentFrameIndex = 0
        else:
            self.currentFrameIndex += 1
