import commands
import playerinfo

class Brain():
    _commands=None
    _playerinfo=None

    def __init__(self):
        self._commands = commands.Commands()
        self._playerinfo = playerinfo.Playerinfo()

    def getPlayerInfo(self):
        return self._playerinfo.get()



