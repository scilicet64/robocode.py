import configuration

class Commands:
    def __init__(self):
        self.__data = {}

    def turn(self, angle):
        if(abs(angle)>configuration.MAX_TURN):
            print("WARNING turn angle too large")
        if ('turn' in self.__data.keys()): print ("WARNING: turn already set this tick")
        self.__data.update({'turn': angle})

    def move(self, distance):
        if(abs(distance)>configuration.MAX_MOVE):
            print("WARNING move distance too large")
        if ('move' in self.__data.keys()): print ("WARNING: move already set this tick")
        self.__data.update({'move': distance})

    def moveRadar(self,angle):
        if(abs(angle)>configuration.MAX_RADARMOVE):
            print("WARNING radar move too large")
        if ('radar' in self.__data.keys()): print ("WARNING: radar already set this tick")
        self.__data.update({'radar': angle})

    def moveTurret(self,angle):
        if(abs(angle)>configuration.MAX_TURRETMOVE):
            print("WARNING radar move too large")
        if ('turret' in self.__data.keys()): print ("WARNING: turret already set this tick")
        self.__data.update({'turret': angle})

    def fire(self,power):
        if(abs(power)>configuration.MAX_FIRE):
            print("WARNING fire power too large")
        if ('fire' in self.__data.keys()): print ("WARNING: fire already set this tick")
        self.__data.update({'fire': power})

    def displayRadar(self):
        if ('displayRadar' in self.__data.keys()): print ("WARNING: fire already set this tick")
        self.__data.update({'displayRadar': 1})

    def hideRadar(self):
        if ('hideRadar' in self.__data.keys()): print ("WARNING: fire already set this tick")
        self.__data.update({'hideRadar': 1})

    def radarbeam(self,angle):
        if (abs(angle) > configuration.MAX_RADARBEAM) or abs(angle) < configuration.MIN_RADARBEAM :
            print("WARNING radarbeam out of allowed range")
        if ('radarbeam' in self.__data.keys()): print ("WARNING: fire already set this tick")
        self.__data.update({'radarbeam': angle})


    def clear(self):
        self.__data.clear()

    def get(self):
        return self.__data