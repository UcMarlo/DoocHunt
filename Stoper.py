import pygame


#TODO: change this so it can use old time as reference
class Stoper(object):

    def __init__(self):
        self.FRAMES_PER_SECOND = 60 # PCMR
        self.ticks = 0


    def newTick(self):
        self.ticks = pygame.time.get_ticks()
        return self.ticks

    def getCurrentTicks(self):
        return self.ticks
