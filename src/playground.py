from lib import tank
from lib import gameinfo

import sys

import example_tank




game = gameinfo.GameInfo()
#game.addPlayer(mytank.MyTank())
game.addPlayer(example_tank.ExampleTank())
game.addPlayer(example_tank.ExampleTank())
game.addPlayer(example_tank.ExampleTank())
game.addPlayer(example_tank.ExampleTank())
game.addPlayer(example_tank.ExampleTank())
game.start()
tank.done()
sys.exit(0)





