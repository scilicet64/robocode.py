import tank
import math
import gameobjectinfo
import matplotlib
matplotlib.use('Agg')



class Radar(object):
    def __init__(self,name=None,gameobject=None,startPos=None):
        screen = tank.Screen()
        __height = 150
        __width = 400
        self.__maxdist = math.hypot(__width,__height)
        self.__relheading = 0
        name = "radar_" + str(name)
        self.__reflections = []
        self.__gameobject = gameobject
        self.__poly = ((0,0), (__height,__width), (-1.0*__height,__width))
        self.__radarshape = screen.register_shape(name, self.__poly )
        self.__radar = tank.Turtle(shape=self.__radarshape,startPos=startPos,visible=False,undobuffersize=0)
        self.__radar.pencolor("yellow")
        self.__radar.penup()
        self.__radar.extrainfo(gameobjectinfo.Gameobjectinfo(self))
        self.__radar.extrainfo().name(name)
        self.__radar.type("radar")
        self.__radar.fillcolor("red")
        self.__radar.setundobuffer(None)

    def heading(self,heading):
        self.__relheading = heading


    def tick(self):
        self.__radar.setpos( self.__gameobject.pos() )
        self.__radar.setheading(self.__gameobject.heading() + self.__relheading)
        hitobjects = self.__radar.collision(["tank"],self.__maxdist)
        hitobjects.remove(self.__gameobject)
        self.collisions(hitobjects)

    def show(self):
        self.__radar.showturtle()

    def hide(self):
        self.__radar.hideturtle()

    def destroy(self):
        self.__radar.destroy()
        self.__radar=None

    def reflections(self):
        return self.__reflections

    def setbeam(self,angle):
        pass

    def collisions(self,hitobjects):
        # Matplotlib mplPath
        self.__reflections = []

        for hitobject in hitobjects:
            pos = hitobject.pos()
            points = [pos]
            polygon = self.__radar._polytrafo(self.__poly)
            path = matplotlib.path.Path(polygon)
            inside = path.contains_points(points)
            if (inside):
                self.__reflections.append(pos)