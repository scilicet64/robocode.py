import tank
import random
import player
import explosion
import Tkinter
import datetime


class GameInfo(object):
    __Players=[]
    __Gametime=0
    __playing=False


    def __init__(self):
        self.__screen = tank.Screen()
        screen = tank.Screen()
        explosion.Explosion.initialize()  # prebuffer explosions in memory
        screen.register_shape("./images/grass.png")
        screen.bgpic("./images/grass.png")
        screen.tracer(0)  # no animation for building up the game

        """def battle():
            print "hello!"

        # create a toplevel menu
        menubar = Tkinter.Menu(screen._root)
        menubar.add_command(label="Battle", command=battle)
        menubar.add_command(label="Quit", command=screen._root.quit)
        # display the menu
        screen._root.config(menu=menubar)
        """


        random.Random()
        seed = random.getstate()
        restorestate = None #paste output of seed here to reply a certain state
        if restorestate:
            random.setstate(restorestate)

        print("random state:\n" + str(seed))
        print "Game started"

    def getRandPos(self):
        width=(self.__screen.window_width()-30)//3
        height=(self.__screen.window_height()-30)//3
        x= random.randint(-1*width,width)
        y=random.randint(-1*height,height)
        return (x,y)

    def addPlayer(self,newbrain):
        self.__Players.append(player.Player(startPos=self.getRandPos(),startHeading=random.randint(0,360),newbrain=newbrain))

    def getPlayer(self,index):
        return self.__Players[index]

    def checkEnd(self):
        playersalivecount = 0
        for player in self.__Players:
            if (player.status()=="playing"):
                playersalivecount+=1
            if playersalivecount>=2:
                return False
        if (playersalivecount<=1):
            return True
        return False

    def checkAnimations(self):
        for player in self.__Players:
            if player.checkAnimations(): return True
        return False

    def getScores(self):
        scores = []
        accuracy = []
        for player in self.__Players:
            scores_dict = player.score()
            name = player.name()
            scores.append((name,scores_dict["score"]))
            accuracy.append((name, scores_dict["accuracy"]))
        scores.sort(key=lambda s: s[1])
        accuracy.sort(key=lambda s: s[1])
        return scores, accuracy


    def frame(self):
            try: #dont use try for debugging, only for  playing
                a = datetime.datetime.now()
                for player in self.__Players:
                    player.tickfunction()
                self.__screen.update()
                #cleanup dead and unused objects
                for player in self.__Players:
                    player.cleanup()
                b = datetime.datetime.now()
                delta = b-a
                ms = int(delta.total_seconds() * 1000)  # milliseconds
                if ms>=25:
                    wait =0
                else:
                    wait = 25 - ms
                if not self.checkEnd():
                    self.__screen.ontimer(self.frame, wait)
                else:
                    self.__playing=False
                    self.displayscores()
                    self.__screen.ontimer(self.end, 25)
            except Exception as e:
                if self.__screen._RUNNING:
                    print("exception: " + str(e))
                pass

    def start(self):
        self.__screen.update()
        self.__playing=True
        for player in self.__Players:
            player.startThread()
        self.__screen.ontimer(self.frame, 25)

    def end(self):
        try:
            for player in self.__Players:
                player.tickfunction()

            if not self.checkAnimations():
                for player in self.__Players:
                    player.moveTurret(10)
                    player.moveRadar(15)
                    player.right(10)
            self.__screen.update()

            # cleanup dead and unused objects
            for player in self.__Players:
                player.cleanup()
            self.__screen.ontimer(self.end, 10)
        except:
            pass



    def displayscores(self):
        scores, accuracies = self.getScores()
        print ("Score:")
        for name, score in scores:
            print(name, score)
        print ("Accuracy %:")
        for name, accuracy in accuracies:
            print(name, accuracy)
        print("Game end.")

    def stop(self):
        for player in self.__Players:
            player.stopThread()
