# robocode.py

## - a programming game for Python based on Robocode and Turtle.py
***
This game is part of a Python programming course, with assignments and videos(tba)
***

### Goal

Develop the _Brains_ of a tank to **Exterminate!!!** opponents



### Quick guide

1) copy example_tank.py to for example  _mytank.py_ and open it
2) rename class name from ExampleTank to your own Name for example _class MyTank_
3) open playground.py and add import for your file
4) add your own class to battle the example tank for example:  _game.addPlayer(mytank.MyTank())_
5) start learning Python to create a dominating Dalek

---


The template contains a init function where playerinfo can be set. Playername will be shown in game.
The tick function returns every frame update

##

```
from lib import brain
class TemplateTank(brain.Brain):

    def __init__(self):
        brain.Brain.__init__(self)
        self._playerinfo.playerName("Lonely Frozen Wolf")

    def tick(self,data):
        return self._commands.get() # return commands for this tick
```



### Returned data every tick

| key in data:  | description |
|:------------- |:-------------|
| position  |  own direction |
| fireheat |  when bigger than zero, shooting is not possible. The more power u use for firing, the longer you have to wait for your next shot|
| heading | own direction |
| alive |  better keep this True |
| reflections| an array with the positions of possible targets or friends |

_example the data dict inside tick function_
when radar sees a reflection:
Blind Wolf1:{'position': (-544.16,-310.16), 'fireheat': 8.0, 'heading': 145.0, 'alive': True, 'reflections': [(-558.32,4.10)]}

### Commands
The Brains of the robot need to be controlled by your class.
with the Commands interface in the class Brain it is possible to control your tank

| command:  | description |
|:------------- |:-------------|
|**clear**|  clear all commands in the dict|
|**fire**( power ) |  take a shot, the variable power determines how much damage the opponent takes on a hit. The more power u use, the longer you have to wait for a next shot|
|**turn**(angle) | the positive or negative angle your tank base turns (turret and radar moves along) |
|**move**(distance)| the positive(forward) or negative(backwards) distance your tank moves |
|**moveTurret**(angle)| the positive or negative angle your Turret turns (radar moves along) |
|**moveRadar**(angle) | the positive or negative angle your Radar dish turns |
|**radarbeam**(angle)| set the beam of the radar, greater angle |
|**displayRadar**| shows the radar beam for debugging purposes |

example commands:
```
self._commands.fire(20)
self._commands.turn(-5.5)
self._commands.move(-10.2) #
self._commands.moveRadar(5.4)
self._commands.displayRadar()
```

## Current development status
* First commit
* World and dynamics will change, but you can already start developing your bot!
* YES we've got rotating images with Turtle.py and we allow png :-)


## Future work and ideas
* http://robowiki.net/
* Doppler radar (reflection also returns relative speed)
* Team battles
* Landmines
* Obstructions
* More easter eggs in code
* Online Competitions (website)
* Blockchain battle over Sevabit network


## Requirements
we need **matplotlib** for detection of targets in radar and PIL (pillow) library

required libraries can be installed for example with pip:
* pip install matplotlib
* pip install pillow


***
_“Letting it get to you. You know what that’s called? Being alive. Best thing there is. Being alive right now is all that counts.”_



Send me a high-five or star this git if you like this project 8-)
SEVAqwjeHAmS7He3kCuQEBHv9LYN2eAoNXYbrYYEFgPa9bMs99MNKrkbkb7TE6WhRMbgE6cavhrQHLHoSkMkZW6n6UZQAit8tZ6
[https://t.me/sevabit]


