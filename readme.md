# DoocHunt - a bootleg duck hunt game

This game was created for passing the PPP subject at Silesian Technical University.

# Authors:
* Adam Wnuk
* Adam Rosiek
* Tomasz Targiel

# The Game
Game is a loose interpretation of the game Duck Hunt for Nintendo Entertainment System. Noteable files:
* Game.py - main game logic and states.
* DuckHuntSprites.py - classes for managing sprites in game
* Duck.py / Dog.py - clases responsible for managing states of animals ( inherits GameObject )
* GameObject.py - Abstract class helping object management in game
* Stopper - time management class
* Sound - sound management class

Win condition - there is no wind condition at this stage. Each level can end with success (escaped ducks == 0) or failure (escaped ducks > 0 ) represented by the reaction of the dog. Levels continue forever.

# Running
Launch RunGame.py

