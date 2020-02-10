from enum import Enum

import pygame
from Crosshair import Crosshair
from Duck import Duck
from Stoper import Stoper
from AnimalSprites import DuckSprite


class Game(object):

    def __init__(self):
        pygame.init()

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("DoocHunt")
        self.stoper = Stoper()

    #################
        self.oldTime= pygame.time.get_ticks()
        self.kierunek = 1
        self.i = 0
    ##################

        self.run = True
        self.crosshair = Crosshair(self.display, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.ducks = []
        self.groundImage = pygame.image.load("images/ground.png")
        self.tree = pygame.image.load("images/tree.png")

        self.duck1 = DuckSprite( "black" , "right" , 0 )
        self.duck1.setNewPosition( 400 , 300 )

        self.duck2 = DuckSprite( "blue" , "left" , 1 )
        self.duck2.setNewPosition( 100 , 100 )

        self.duck3 = DuckSprite( "brown" , "left_up" , 0 )
        self.duck3.setNewPosition( 500 , 400 )

        self.duck4 = DuckSprite( "brown" , "right_up" , 0 )
        self.duck4.setNewPosition( 100 , 400 )

        self.duck5 = DuckSprite( "black" , "fall" , 0 )
        self.duck5.setNewPosition( 200 , 200 )

        self.duck6 = DuckSprite( "blue" , "fall" , 0 )
        self.duck6.setNewPosition( 200+20 , 200 )

        self.duck7 = DuckSprite( "brown" , "fall" , 0 )
        self.duck7.setNewPosition( 200+40 , 200 )

        self.duck8 = DuckSprite( "black" , "hit" , 0 )
        self.duck8.setNewPosition( 200 , 300 )

        self.duck9 = DuckSprite( "blue" , "hit" , 0 )
        self.duck9.setNewPosition( 200+20 , 300 )

        self.duck10 = DuckSprite( "brown" , "hit" , 0 )
        self.duck10.setNewPosition( 200+40 , 300 )

        self.duck11 = DuckSprite( "black" , "up" , 0 )
        self.duck11.setNewPosition( 500 , 300 )

        self.duck12 = DuckSprite( "blue" , "up" , 0 )
        self.duck12.setNewPosition( 500+20 , 300 )

        self.duck13 = DuckSprite( "brown" , "up" , 0 )
        self.duck13.setNewPosition( 500+40 , 300 )

        self.ducksS = pygame.sprite.Group()
        self.ducksS.add(self.duck1)
        self.ducksS.add(self.duck2)
        self.ducksS.add(self.duck3)
        self.ducksS.add(self.duck4)
        self.ducksS.add(self.duck5)
        self.ducksS.add(self.duck6)
        self.ducksS.add(self.duck7)
        self.ducksS.add(self.duck8)
        self.ducksS.add(self.duck9)
        self.ducksS.add(self.duck10)
        self.ducksS.add(self.duck11)
        self.ducksS.add(self.duck12)
        self.ducksS.add(self.duck13)
        self.ducksS.update()


    # TODO: it looks awful, is there a good looking switch case?
    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print("mouse: ", mx, my)

    def main_loop(self):
        self.setup_round(1)
        #TODO: prepare scene before main loop
        while self.run:
            dt = self.stoper
            self.crosshair.move(pygame.mouse.get_pos())

            for event in pygame.event.get():
                self.__handle_event(event)

            self.tick()
            self.render_and_display_frame()
        return None

    def render_and_display_frame(self):
        self.render_background()
        self.render_ducks()
        self.crosshair.render()

        self.ducksS.update()
        self.ducksS.draw(self.display)

        pygame.display.update()

    def render_background(self):
        black = (80, 80, 130)  # TODO: background
        self.display.fill(black)

    def spawn_duck(self):
        duck = Duck(self.display, self.stoper, (250,250), pygame.image.load("images/duck.jpg"))
        self.ducks.append(duck)


    #TODO: theres a good place to setup a state machine - e.g. STARTING_TURN, TURN, WON_TURN, LOST_TURN etc.
    def tick(self):

        for duck in self.ducksS:
            duck.nextFrame()



            self.duck1.move(5 * self.kierunek ,0)
            self.duck2.move(-5 * self.kierunek ,0)
            self.duck3.move(-5 * self.kierunek ,-5 * self.kierunek)
            self.duck4.move(+5 * self.kierunek ,+5 * self.kierunek)

            self.oldTime = pygame.time.get_ticks()

            self.i += 1

            if self.i > 30:
                self.i = 0
                self.kierunek *= -1

                for duck in self.ducksS:
                    duck.reverseDirection()

        self.execute_ducks_logic()
        pass

    def execute_ducks_logic(self):
        for duck in self.ducks:
            duck.tick()

    def render_ducks(self):
        for duck in self.ducks:
            duck.render()

    def render_background(self):
        blue = (60, 80, 150) #TODO: background
        self.display.fill(blue)
        rect = self.groundImage.get_rect()
        self.display.blit(self.groundImage, (0, self.SCREEN_HEIGHT - rect.height ))
        return None

    class GameState(Enum):
        STARTING = 0
        ROUND_START = 1
        ACTIVE_GAME = 2
        ROUND_END = 3
        GAME_END = 4

    def setup_round(self, level):
        self.spawn_duck()
        return None
