import pygame


class Duck(object):

    #TODO: make it use sprites instead of image
    def __init__(self, display, startingX, startingY):
        self.gameDisplay = display
        self.position = (startingX, startingY)
        self.image = pygame.image.load("images/duck.jpg")
        #self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.imageCenterX = self.image.get_height() / 2
        self.imageCenterY = self.image.get_width() / 2


    def move(self, pos):
        x,y = pos
        self.mousePosition = (x - self.imageCenterX), (y - self.imageCenterY)

    def tick(self):
        #TODO: create some "AI" logic

        #TODO: duck can "bounce" of the vertical walls of the screen. I think they might also bounce of, of the other ducks
        return None

    def render(self):
        self.gameDisplay.blit(self.image, self.position)
