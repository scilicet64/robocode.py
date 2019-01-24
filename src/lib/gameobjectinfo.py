class Gameobjectinfo(object):
    def __init__(self,playerClass):
        self.__name = None
        self.__animation = None
        self.playerClass(playerClass)
        self.__markdestroy = False




    def name(self,name=None):
        if (name==None):
            return self.__name
        else:
            self.__name=name

    def power(self,power=None):
        if (power==None):
            return self.__power
        else:
            self.__power=power

    def playerClass(self,playerClass=None):
        if (playerClass==None):
            return self.__playerClass
        else:
            self.__playerClass=playerClass

    def animation(self,animation=None):
        if (animation==None):
            return self.__animation
        else:
            self.__animation=animation

    def hitobject(self,hitobject=None):
        if (hitobject==None):
            return self.__hitobject
        else:
            self.__hitobject=hitobject

    def markdestroy(self):
        """mark object to be destroyed after processing"""
        """seperate get and set to avoid confusion"""
        self.__markdestroy=True

    def ismarkeddestroy(self):
        """mark object to be destroyed after processing"""
        """seperate get and set to avoid confusion"""
        return self.__markdestroy