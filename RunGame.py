from Game import Game
import sys
import os

if sys.platform.startswith('darwin'):
    os.chdir('/Applications/DoocHunt.app/Contents/Resources')

g = Game()
g.main_loop()
