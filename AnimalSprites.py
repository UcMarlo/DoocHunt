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
        filePath = "images/" + duckColor + "_duck/" + duckAnimationSet + ".gif"
        return [pygame.image.load(filePath).convert()]

    def _prepareAnimationCollection(self, duckColor, duckAnimationSet, imageCount):
        collection = []
        for i in range(imageCount):
            filePath = "images/" + duckColor + "_duck/" + duckAnimationSet + "_" + str(i) + ".gif"
            collection.append(pygame.image.load(filePath).convert())
        return collection

    def _prepareSpriteMapForColor(self, duckColor):
        spriteCollection = {}
        spriteCollection[DuckAnimationState.FALLING] = self._prepareOneFrameCollection(duckColor, DuckAnimationState.FALLING)
        spriteCollection[DuckAnimationState.HIT] = self._prepareOneFrameCollection(duckColor, DuckAnimationState.HIT)
        spriteCollection[DuckAnimationState.HORIZONTAL] = self._prepareAnimationCollection(duckColor, DuckAnimationState.HORIZONTAL, 3)
        spriteCollection[DuckAnimationState.DIAGONAL] = self._prepareAnimationCollection(duckColor, DuckAnimationState.HORIZONTAL, 3)
        spriteCollection[DuckAnimationState.UP] = self._prepareAnimationCollection(duckColor, DuckAnimationState.HORIZONTAL, 3)
        return spriteCollection

class RepeatingSpriteSet(object):
    def __init__(self, frames):
        self.frames = frames
        self.currentFrameIndex = 0
        self.animationIncrement = 1
        self.maxFrames = len(frames)

    def getFrame(self):
        return self.frames[self.currentFrameIndex]

    def nextFrame(self):
        if self.currentFrameIndex == self.maxFrames or self.currentFrameIndex == 0:
            self.animationIncrement = -self.animationIncrement
        self.currentFrameIndex += self.animationIncrement



class DuckSprite(pygame.sprite.Sprite):
    # Class for a sprite of a duck.
    def __init__(self, color, startState , startAnimationFrame):
        super().__init__()

        self.color = color
        self.state = startState
        self.animationFrame = startAnimationFrame

        self.image = getImageOfDuck( color , startState , startAnimationFrame)

        self.rect = self.image.get_rect()

    def updateImage(self):
        self.image = getImageOfDuck( self.color , self.state , self.animationFrame )

    def nextFrame(self):
        self.animationFrame += 1
        if( self.animationFrame >= MAX_DUCK_ANIMATION_FRAMES):
            self.animationFrame = 0
        self.updateImage()        
    
    def setNewState(self, state):
        self.state = state
        self.frame = 0
        self.updateImage()

    def setNewPosition( self, x , y ):
        self.rect.center = (x,y)
    
    def move(self , x, y):
        self.rect.x += x
        self.rect.y += y

    def reverseDirection(self):
        if self.state == "left":
            self.state = "right"
        elif self.state == "right":
            self.state = "left"
        elif self.state == "right_up":
            self.state = "left_up"
        elif self.state == "left_up":
            self.state = "right_up"
        
        self.updateImage()

