import commands
import playerinfo
from time import sleep
import random

class Brain(object):
    _commands=None
    _playerinfo=None
    __playerclass=None
    __commandAllowed= False


    def __init__(self):
        self.__Alive=True
        self._commands = commands.Commands()
        self._playerinfo = playerinfo.Playerinfo()

    def getPlayerInfo(self):
        return self._playerinfo.get()

    def start(self,arg):
        self.__playerclass=arg
        while(self.__Alive):
            self.run()

    def stop(self):
        ###called when game is closed to stop thread
        self.__Alive = False

    def doNothing(self):
        sleep(1)

    def waitforTurn(self):
        wait=True
        sleep(1)
        pass

    def forward(self, distance):
        self.waitforTurn()

    def tick(self, data):
        self.__Alive = data.get("alive")
        #print(self._playerinfo.playerName()+ ":" + str(data))  # show available tick data
        # implement brains
        # for example
        self._commands.clear()
        power = 1  # random.randint(0,20)
        self._commands.fire(power)
        angle = -6
        self._commands.turn(angle)
        distance = 6
        self._commands.move(distance)
        angle = random.randint(0, 5)
        self._commands.moveTurret(angle)
        self._commands.moveRadar(5)
        #if ("1" in self._playerinfo.playerName()):
        #    self._commands.displayRadar()
        return self._commands.get()  # return commands for this tick


