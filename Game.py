import pygame
from Crosshair import Crosshair


class Game(object):

    def __init__(self):
        pygame.init()

        self.SCREEN_HEIGHT = 500
        self.SCREEN_WIDTH = 500

        self.display = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
        pygame.display.set_caption("DoocHunt")

        self.run = True
        self.crosshair = Crosshair(self.display, self.SCREEN_HEIGHT, self.SCREEN_WIDTH)

    # TODO: it looks awful, is there a good looking switch case?
    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print("mouse: ", mx, my)

    def main_loop(self):
        while self.run:
            self.crosshair.move(pygame.mouse.get_pos())

            for event in pygame.event.get():
                self.__handle_event(event)

            # Render n stuff
            black = (0,0,0)
            self.display.fill(black)
            self.crosshair.render()
            pygame.display.update()
        return None
