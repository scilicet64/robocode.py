import tank
import gameobjectinfo

class LifeBar():
    def __init__(self,name=None):
        screen = tank.Screen()
        __height = 3
        __width = 100
        name = "lifebar_" + str(name)
        self.__lifeshape = screen.register_shape(name, ((__height,0), (__height,__width), (0,__width), (0,0)) )
        self.__lifebar = tank.Turtle(shape=self.__lifeshape,undobuffersize=0)
        self.__lifebar.pencolor("black")
        self.__lifebar.pen(resizemode="user",stretchfactor=(1,1))
        self.__lifebar.penup()
        self.__lifebar.extrainfo(gameobjectinfo.Gameobjectinfo(self))
        self.__lifebar.extrainfo().name(name)
        self.__lifebar.type("lifebar")
        self.__lifebar.setundobuffer(None)
        self.setLifescore(100)


    def setLifescore(self,lifescore):
        if (lifescore>0):
            stretchfactor_width = lifescore/100.0
        else:
            stretchfactor_width=0
        if (lifescore < 30):
           self.__lifebar.fillcolor("red")
        elif (lifescore < 40):
           self.__lifebar.fillcolor("orange")
        elif (lifescore < 70):
           self.__lifebar.fillcolor("yellow")
        else:
           self.__lifebar.fillcolor("green")
        self.__lifebar.pen(resizemode="user",stretchfactor=(1,stretchfactor_width))

    def setpos(self,pos):
        self.__lifebar._position = pos
        self.__lifebar.setpos(pos)

    def destroy(self):
        self.__lifebar.clear()
        self.__lifebar.destroy()
        self.__lifebar==None

    def hide(self):
        self.__lifebar.hideturtle()