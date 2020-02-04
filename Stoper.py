import pygame

class Stoper(object):

    def __init__(self):
        self.FRAMES_PER_SECOND = 60 # PCMR
        self.clock = pygame.time.Clock()
        self.dt = 0


    def newTick(self):
        self.dt = self.clock.tick(60)
        return self.dt

    def getCurrentDt(self):
        return self.dt
