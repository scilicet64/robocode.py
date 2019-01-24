import tank
import gameobjectinfo
import explosion

class Bullet(object):
    def __init__(self,startpos,name,power,heading,localtank):
        screen = tank.Screen()
        self.__bulletshape =screen.register_shape("./images/bullet.png")
        self.__turtle=tank.Turtle(
                           shape=self.__bulletshape,
                           undobuffersize=0,
                           visible=True,
                           startPos=startpos
                           )
        self.__localtank = localtank
        self.__hitpoints = 0
        self.extrainfo(gameobjectinfo.Gameobjectinfo(self))
        self.extrainfo().name(name)
        self.extrainfo().power(power)
        self.__turtle.type("bullet")
        self.__turtle.setundobuffer(None)
        self.__turtle.penup()
        self.__turtle.setheading(heading)
        self.__turtle.forward(1)
        self.__turtle.speed(1)

    def not_exploded(self):
        return (self.extrainfo().animation()==None)

    def exploded(self):
        return (self.extrainfo().animation().status()=="done")

    def extrainfo(self,info=None):
        if (info==None):
            return self.__turtle.extrainfo()
        else:
            return self.__turtle.extrainfo(info)

    def processCollision(self):
        self.__turtle.forward(10)
        hitobjects = self.__turtle.collision(["tank"],22)
        for hitobject in hitobjects:
            if (hitobject != None and hitobject != self.__localtank):
                power = self.extrainfo().power()

                #print (self.extrainfo().name() + " power:" + str(power) + " " + hitobject.extrainfo().playerClass().name())
                self.extrainfo().hitobject(hitobject)
                self.__hitpoints = power #single time scoring
                if (hitobject.extrainfo().playerClass().hit(power)) > 0:
                    self.extrainfo().animation(explosion.Explosion("small",self))
                else:
                    self.extrainfo().animation(explosion.Explosion("big",self))


    def hitpoints(self):
        return self.__hitpoints

    def processEnd(self):
        if not self.extrainfo().ismarkeddestroy():
            self.extrainfo().animation(None)

    def markdestroy(self):
        self.extrainfo().markdestroy()
        self.__turtle.hideturtle()


    def destroy(self):
        if self.extrainfo().ismarkeddestroy():
            self.__turtle.destroy() # mark for destroy

    def isOncanvas(self):
        return self.__turtle.isOncanvas()

    def shape(self,shape):
        self.__turtle.shape(shape) # to set explosion shape

    def extrainfo(self, info=None):
        if (info == None):
            return self._extrainfo
        else:
            self._extrainfo = info