class Playerinfo:
    """Info on the player"""
    def __init__(self):
        self.__data = {}
        pass

    def playerName(self,playername):
        self.__data.update({'playername': playername})

    def teamName(self,teamname):
        self.__data.update({'teamname': teamname})

    def clear(self):
        self.__data.clear()

    def get(self):
        return self.__data