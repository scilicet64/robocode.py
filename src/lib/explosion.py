import tank


class Explosion(object):
    __status = "init"
    __MAXFRAME = 71
    __frames = ["empty_startframe"]

    def __init__(self, type, target):
        self.__factor = 2
        self.__framenr = 0
        self.__type = type
        self.__target=target
        Explosion.initialize()
        if(type=="small"):
            self.triggerSmall()
        else:
            self.triggerBig()


    @staticmethod
    def getPath(framenr):
        return "./images/explosions/explosion2-"+str(framenr)+".png"

    @staticmethod
    def getShape(framenr):
        return Explosion.__frames[framenr]

    @staticmethod
    def initialize():
        if Explosion.__status=="init":
            for x in range(1,Explosion.__MAXFRAME+1):
                bulletshape = tank.Screen().register_shape(Explosion.getPath(x))
                Explosion.__frames.append(bulletshape)
            Explosion.__status="initialized"

    def tick(self):
        #show current frame and set next framenr
        if (self.__framenr<=(self.__endframe*self.__factor)):
            self.show((self.__framenr // self.__factor) +1)
            self.__framenr+=1




    def triggerSmall(self):
        self.__endframe = 30
        self.__framenr =1

    def triggerBig(self):
        self.__endframe = self.__MAXFRAME
        self.__framenr = 1

    def show(self,framenr):
        framenr = framenr
        if (framenr>0) and (framenr < self.__endframe):
            self.__target.shape(Explosion.getShape(framenr))
        else:
            print("problem")

    def status(self):
        if (self.__framenr==0):
            return "init"
        elif (self.__framenr>=self.__endframe*(self.__factor-1)):
            return "done"
        else: return "playing"