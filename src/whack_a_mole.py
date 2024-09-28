import random, threading, time, queue
from ydl import Client
from utils import *

NUM_OF_LIGHTS = 3
rd = random.Random()
rd.seed(16383)
q = queue.Queue()
yc = Client(YDL_TARGETS.SHEPHERD)
# Question 1-2: Set Up the "Board"
# BEGIN Q1
lights = []
# END Q1


def wrapper(s: str):
    match s:
        case 'a':
            return str(0)
        case 's':
            return str(1)
        case 'd':
            return str(2)
        case _:
            return s

def keyboard_input():
    while True:
        line = wrapper(input())
        # Question 2-2: Treat Keyboard Input
        # BEGIN Q2
        if ____:
            ____
        # END Q2
            yc.send(SHEPHERD_HEADER.BUTTON_PRESS(id=int(line)))


def whack(n: int):
    # Question 6: Whack The Mole...?
    # BEGIN Q6
    pass    # Delete this line
    # END Q6


def turn_on(n: int):
    # Question 7-1: Turn On the Light
    # BEGIN Q7
    pass    # Delete this line
    # END Q7
    
def turn_off(n: int):
    # Question 7-2: Turn Off the Light
    # BEGIN Q7
    pass    # Delete this line
    # END Q7


def moles():
    """
    Randomly assigns a mole to pop up.
    """
    # Question 8: Mole Popping Up - Revisited
    # BEGIN Q8
        # Why is it Q8 this time, not Q4?
    # END Q8

def whack_a_mole():
    print("Welcome to Whack A Mole! \nLet's start a game!\n\n")
    time.sleep(.5)
    interval = .75
    correct = True
    try:
        while correct:
            while not q.empty(): q.get()        # clear the queue, avoid vibro-tapping
            waited = 0
            correct = False
            # Question 9: Activate Mole
            # BEGIN Q9
                # Call some function here
            # END Q9
            while not q.empty() or waited < interval:
                waited += 0.01
                time.sleep(0.01)
                # Question 10: Trial to Pull Keyboard Input
                # BEGIN Q10
                    # Suggestion: try out the try-catch block
                # END Q10

                # Question 11: Whacking Logic
                    # Previously embedded in Q3
                # BEGIN Q11
                if ____:
                    ____
                    # correct = False   # Not Necessary
                    raise StopIteration
                else:
                    ____
                    time.sleep(.2)
                    correct = True
                    break
                # END Q11
            if not correct:
                raise StopIteration
    except StopIteration:
        # Question 12: End of Game
        # BEGIN Q12
            # Turn off all the lights; then end of loop
        # END Q12
        time.sleep(1)
    print("\nEnd of game. Thanks for playing!")


threading.Thread(target=keyboard_input, args=(), daemon=True).start()
whack_a_mole()
