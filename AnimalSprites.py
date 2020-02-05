import pygame

MAX_DUCK_ANIMATION_FRAMES = 3
colors = ("blue","black","brown")
duck_physical_states = ("fall","hit","right","right_up","up")
duck_virtual_states = ("left", "left_up")
duck_states = duck_physical_states + duck_virtual_states
frameles_states = ("fall","hit")

PLACE_HOLDER = "images/error.png"


def getImageOfDuck( color , state , frame):
    rotate = 0
    pathToFile = PLACE_HOLDER
    if (color in colors) and (state in duck_states) and (frame < MAX_DUCK_ANIMATION_FRAMES):
        if state in duck_virtual_states:
            rotate = 1
            if state == "left":
                state = "right"
            elif state == "left_up":
                state = "right_up"
        if state in frameles_states:
            frame = 0
        pathToFile = "images/" + color + "_duck/" + state + "_" + str(frame+1) + ".gif"
    
    image = pygame.image.load(pathToFile).convert()
    if rotate:
        image = pygame.transform.flip(image , 1 , 0)
    return image



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
    #    self.rect = self.image.get_rect()

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

