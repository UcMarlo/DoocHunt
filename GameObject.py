import pygame

class GameObject(object):

    def __init__(self, display, stoper, position, image):
        self.position = position
        self.gameDisplay = display
        self.stoper = stoper
        self.renderable = True
        self.image = image

    def tick(self):
        return None

    def render(self):
        if (self.renderable):
            self.gameDisplay.blit(self.image, self.position)
        return None
