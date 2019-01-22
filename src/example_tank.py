from lib import brain
import random

class ExampleTank(brain.Brain):
    __playerNumber = 0

    def __init__(self):
        ExampleTank.__playerNumber += 1
        self.__playerName = "Blind Wolf" + str(ExampleTank.__playerNumber)
        brain.Brain.__init__(self)
        self._playerinfo.playerName(self.__playerName)
        #self._playerinfo.teamName("Red")

    def tick(self,data):
        #print(self.__playerName + ":"+ str(data))# show available tick data
        #implement brains
        #for example
        self._commands.clear()
        power = 1# random.randint(0,20)
        self._commands.fire(power)
        angle = -3.0
        self._commands.turn(angle)
        distance = random.randint(0,4)
        self._commands.move(distance)
        angle = random.randint(0,5)
        self._commands.moveTurret(angle)
        self._commands.moveRadar(6)
        if ("1" in self.__playerName):
            self._commands.displayRadar()

        return self._commands.get() # return commands for this tick