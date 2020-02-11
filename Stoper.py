import pygame


#TODO: change this so it can use old time as reference
class Stoper(object):

    def __init__(self):
        self.FRAMES_PER_SECOND = 60 # PCMR
        self.clock = pygame.time.Clock()
        self.ticks = 0
        self.delta = 0

    def newTick(self):
        self.ticks = pygame.time.get_ticks()
        self.delta = self.clock.tick(self.FRAMES_PER_SECOND)
        return self.ticks

    def getDetla(self):
        return self.delta

    def getCurrentTicks(self):
        return self.ticks
