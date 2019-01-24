class Playerinfo(object):
    """Info on the player"""
    def __init__(self):
        self.__data = {}
        pass

    def playerName(self,playername=None):
        if(playername is None):
            return self.__data.get('playername')
        else:
            self.__data.update({'playername': playername})

    def teamName(self,teamname):
        if (teamname is None):
            return self.__data.get('teamname')
        else:
            self.__data.update({'teamname': teamname})

    def clear(self):
        self.__data.clear()

    def get(self):
        return self.__data