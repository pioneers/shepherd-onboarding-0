from ydl import Client, Handler
from utils import *


yc = Client(YDL_TARGETS.SHEPHERD)
yh = Handler()
NUM_OF_LIGHTS = 3
# Question 1-3: Set Up the "Board"
# BEGIN Q1
lights = []
# END Q1
_print = True


@yh.on(SHEPHERD_HEADER.TURN_ON_BUTTON_LIGHT)
def turn_on_button_light(id: int):
    # Question 7-3: Turn On the Light
    # BEGIN Q7
    pass    # Delete this line
    # END Q7

@yh.on(SHEPHERD_HEADER.TURN_OFF_BUTTON_LIGHT)
def turn_off_button_light(id: int):
    # Question 7-4: Turn Off the Light
    # BEGIN Q7
    pass    # Delete this line
    # END Q7


while True:
    if (_print):
        _print = False
        print(''.join(["          " + ("@" if lights[n] else "-") for n in range(NUM_OF_LIGHTS)]))
    msg = yc.receive()
    _print = yh.handle(msg)
