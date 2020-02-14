import pygame

class GameObject(object):

    def __init__(self, display, stoper, positionVector):
        self.positionVector = positionVector
        self.gameDisplay = display
        self.stoper = stoper
        self.renderable = True
        self.animationIntervalInMs = 100
        self.image = None
        self.currentImageSet = None

    def tick(self):
        self.changeAnimationFrame()
        return None

    def render(self):
        if (self.renderable):
            self.gameDisplay.blit(self.image, self.positionVector)
        return None

    def move(self, x, y):
        self.positionVector = (x, y)

    def changeAnimationFrame(self):
        if self.stoper.getCurrentTicks() - self.lastAnimationUpdate > self.animationIntervalInMs:
            self.currentImageSet.nextFrame()
            self.lastAnimationUpdate = self.stoper.getCurrentTicks()
            self.image = self.currentImageSet.getFrame()

    def forceChangeAnimationFrame(self):
        self.currentImageSet.nextFrame()
        self.lastAnimationUpdate = self.stoper.getCurrentTicks()
        self.image = self.currentImageSet.getFrame()