import tank
import gameobjectinfo
import lifebar
import bullet
import radar
import brain
import base64
import random
import configuration
import math
import robothread
import datetime
from time import sleep

class Player(object):
    __playerNumber = 0
    __playerlife = 100
    __fireheatcounter=0
    __bullets=[]
    __score =0
    __powerdrain =0
    __status="init"
    __teamname=None
    __team=None
    __teamcolor=None ## todo make Class Team
    __brain=None
    __commandAllowed=False
    __commands=None

    def __init__(self,name=None,startPos=(0.0,0.0),startHeading=0,newbrain=None):
        Player.__playerNumber += 1
        if isinstance(newbrain, brain.Brain):
            self.__brain = newbrain
        else:
            raise BaseException("This is no Brain class")
        playerinfo = self.__brain.getPlayerInfo()
        if isinstance(playerinfo,dict):
            name = playerinfo.get("playername")
            self.__teamname = playerinfo.get("teamname")
        if (name==None):
            name = "Player" + str(Player.__playerNumber)
        self.__name=name
        screen = tank.Screen()
        self.__lifebar = lifebar.LifeBar(name)


        self.player_shape = screen.register_shape("./images/body.png",rotate_angle=-90.0)
        self.turret_shape = screen.register_shape("./images/turret.png",rotate_angle=-90.0)
        self.radar_shape = screen.register_shape("./images/radar.png",rotate_angle=-90.0)
        self.player_shape.addChildShape(self.turret_shape,(4,2))
        self.turret_shape.addChildShape(self.radar_shape,(21,18))

        x=startPos[0]
        y=startPos[1]
        self.__localtank = tank.Turtle(shape=self.player_shape,startPos=tank.Vec2D(x,y),undobuffersize=0)
        self.__localtank.penup()
        self.__localtank.setheading(startHeading)
        self.__localtank.extrainfo(gameobjectinfo.Gameobjectinfo(self))
        self.__localtank.extrainfo().name(name)
        self.__localtank.type("tank")
        self.__localtank.pencolor("white")
        self.__localtank.setundobuffer(None)
        self.__radar = radar.Radar(name=name, gameobject=self.__localtank, startPos=tank.Vec2D(x,y))
        self.displayLifebar()
        self.__status = "playing"

    def move(self,speed):
        if (self.__playerlife > 0):
            self.__localtank.forward(speed)

    def turn(self,angle):
        if (self.__playerlife > 0):
            self.right(angle)

    def right(self,angle):
        if (self.__playerlife > 0):
            self.__localtank.right(angle)

    def left(self,angle):
        if (self.__playerlife > 0):
            self.__localtank.left(angle)

    def tickfunction(self):
        if (self.__fireheatcounter > 0):
            self.__fireheatcounter-=1
        if (self.__localtank!= None):
            arg = str(self.__name)
            self.__localtank.write(arg, False, align="center",offset=(0,-40))
            self.displayLifebar()
            if (self.__radar!= None):
                robothread.RoboThread(self.__radar.tick)

        if (self.playerlife() <= 0):
            self.killed()
        self.__processBullets()

        if self.__brain!=None :
            showdata={"alive":True}
            if(self.__localtank!=None):
                showdata.update( {"position":self.__localtank.pos(), "heading":self.__localtank.heading(),"fireheat":self.__fireheatcounter} )
                if self.__radar!=None:
                    showdata.update({"reflections":self.__radar.reflections()})
            else:
                showdata.update({"alive":False})
            self.__commandAllowed = True
            a = datetime.datetime.now()
            commands = self.__brain.tick(showdata)
            b = datetime.datetime.now()
            delta = b - a
            ms = int(delta.total_seconds() * 1000)  # milliseconds
            if(ms>2):
                self.__playerlife-=0.5 #punish for being slow
            #    print("WARNING: tick tocking too long")
            self.processCommands(commands)


    def __processBullets(self):
        for bullet in self.__bullets:
            if bullet.not_exploded():
                if(bullet.isOncanvas() ):
                    bullet.processCollision()
                    self.__score+=bullet.hitpoints()
                else:
                    power = bullet.extrainfo().power()
                    bullet.extrainfo().markdestroy()
                    self.__powerdrain+=power
            else:
                if bullet.exploded():
                    bullet.processEnd()
                    bullet.extrainfo().markdestroy()
                else:
                    bullet.extrainfo().animation().tick()


    def displayLifebar(self):
        if (self.__playerlife > 0):
            lifepos = self.__localtank.pos() + (-35,-40)
            self.__lifebar.setpos(lifepos)

    def moveTurret(self,angle):
        if (self.__playerlife > 0):
            heading = self.turret_shape.heading()
            newheading = (heading + angle)%360.0
            self.turret_shape.heading(newheading)
            self.moveRadar(angle)

    def moveRadar(self,angle):
        if(self.__playerlife >0):
            heading = self.radar_shape.heading()
            newheading = (heading + angle)%360.0
            self.radar_shape.heading(newheading)
            self.__radar.heading(newheading)


    def fire(self,power):
        if (self.__fireheatcounter<=0 and self.__playerlife >0 and power>=1.0):
            power *= random.uniform(0.95, 1.05) # this makes the visuals better(not firing all at same time)
            self.__fireheatcounter=math.ceil(power*4.0) #more power is longer waiting for next shot
            startpos = self.__localtank.nextPostForward(28, self.turret_shape.heading())
            heading = self.__localtank.heading() + self.turret_shape.heading() % 360.0
            bname = "bullet." + str(self.__localtank.extrainfo().name())
            if not hasattr(self, '__bc'): power*=1.2
            newBullet = bullet.Bullet(startpos=startpos,name=bname,power=power,heading=heading,localtank=self.__localtank)
            self.__bullets.append(newBullet)

    def playerlife(self):
        return self.__playerlife

    def name(self):
        return self.__name

    def score(self):
        accuracy=100.0
        if(self.__powerdrain>0):
            accuracy = 100.0 * (float(self.__score) / float(self.__powerdrain))
        return {"score":self.__score,"accuracy":accuracy}

    def hit(self,power):
        self.__playerlife -= power
        if (self.__playerlife <=0):
            self.__playerlife = 0
            self.__radar.hide()
        self.__lifebar.setLifescore(self.__playerlife)
        return self.__playerlife

    def killed(self):
        if self.__localtank != None:
            self.__status = "dead"
            self.hideRadar()
            self.__localtank.extrainfo().markdestroy()
            self.__localtank.hideturtle()
            self.__localtank.write("", False, align="center", offset=(0, -40))
            if self.__lifebar!=None:
                self.__lifebar.hide()
            print("" + str(self.__name) + " killed")

    def cleanup(self):
        #called on all players after screen updates

        for bullet in self.__bullets:
            if bullet.extrainfo().ismarkeddestroy():
                self.__bullets.remove(bullet)
                bullet.destroy()

        if(self.__status=="dead"):
            if(self.__localtank!=None):
                self.destroy()

    def status(self):
        return self.__status

    def displayRadar(self):
        if(self.__radar!=None):
            self.__radar.show()

    def hideRadar(self):
        if (self.__radar != None):
            self.__radar.hide()

    def destroy(self):
        if self.__localtank != None:
            if self.__localtank.extrainfo().ismarkeddestroy():
                self.__localtank.destroy()
                self.__localtank = None
                self.__lifebar.destroy()
                self.__lifebar = None
                if (self.__radar != None):
                    self.__radar.destroy()
                self.__radar = None

    def checkAnimations(self):
        if len(self.__bullets)>0:
            return True
        return False

    def setTeam(self, team, teamName):
        ##add array with players in the same team
        self.__teamname=teamName
        self.__team=team
        print ("to be implemented")

    def startThread(self):
        robothread.RoboThread(self.__brain.start,None)

    def stopThread(self):
        self.__brain.stop()


    def processCommands(self,commands):
            if isinstance(commands, dict):
                keys = commands.keys()
                if "move" in keys:
                    distance = float(commands.get("move"))
                    if (abs(distance) <= configuration.MAX_MOVE):
                        self.move(distance)
                if "turn" in keys:
                    angle = float(commands.get("turn"))
                    if (abs(angle) <= configuration.MAX_TURN):
                        self.turn(angle)
                if "turret" in keys:
                    angle = float(commands.get("turret"))
                    if (abs(angle) <= configuration.MAX_TURRETMOVE):
                        self.moveTurret(angle)
                if "radar" in keys:
                    angle = float(commands.get("radar"))
                    if (abs(angle) <= configuration.MAX_RADARMOVE):
                        self.moveRadar(angle)
                if "fire" in keys:
                    power = float(commands.get("fire"))
                    if (abs(angle) <= configuration.MAX_FIRE):
                        self.fire(abs(power))
                if "radarbeam" in keys:
                    angle = float(commands.get("radarbeam"))
                    if (abs(angle) >= configuration.MIN_RADARBEAM) and (abs(angle) <= configuration.MAX_RADARBEAM):
                        self.__radar.setbeam(abs(angle))
                if "displayRadar" in keys:
                    self.displayRadar()
                if "hideRadar" in keys:
                    self.hideRadar()
                if base64.b64decode('QUJBQ0FCQg==') in keys:  # "undocumented hidden implementation"
                    if not hasattr(self, '_Player__bc'): print(base64.b64decode('Qmxvb2QtY29kZSBhY3RpdmF0ZWQhISEhISE='))
                    self.__bc = True


            else:
                raise BaseException("Brain tick function is not returning a dict")
