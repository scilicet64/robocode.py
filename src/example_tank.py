from lib import brain
import random

class ExampleTank(brain.Brain):
    __playerNumber = 0

    def __init__(self):
        ExampleTank.__playerNumber += 1
        playerName = "Blind Wolf" + str(ExampleTank.__playerNumber)
        brain.Brain.__init__(self)
        self._playerinfo.playerName(playerName)

        #self._playerinfo.teamName("Red")



    def run(self):
        self.doNothing()
        self.forward(100)



