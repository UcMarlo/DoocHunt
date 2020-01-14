import  pygame

class Crosshair(object):

    def __init__(self, display, screenHeight, screenWidth):
        self.gameDisplay = display
        self.mousePosition = (screenHeight / 2, screenWidth / 2)
        self.image = pygame.image.load("images/crosshair.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1) # TODO: This shouldn't be hardcoded
        self.imageCenterX = self.image.get_height() / 2
        self.imageCenterY = self.image.get_width() / 2



    def render(self):
        self.gameDisplay.blit(self.image, self.mousePosition)

    def move(self, pos):
        x,y = pos
        self.mousePosition = (x - self.imageCenterX), (y - self.imageCenterY)




