import random

NUM_OF_LIGHTS = 5
rd = random.Random()
rd.seed(16383)
# Question 1-1: Set Up the "Board"
# BEGIN Q1
lights = []
# END Q1


def wrapper(s: str):
    """
    Wrapper function to treat certain inputs as others.
    """
    match s:
        case 'a':
            return str(0)
        case 's':
            return str(1)
        case 'd':
            return str(2)
        case 'f':
            return str(3)
        case 'g':
            return str(4)
        case _:
            return s

def keyboard_input():
    """
    Read the keyboard input and whack the mole if applicable.
    """
    line = wrapper(input())
    # Question 2-1: Treat Keyboard Input
    # BEGIN Q2
    if ____:
        ____
    # END Q2

def whack(n: int):
    """
    Whack the mole located at *n*.
    """
    # Question 3: Whack The Mole!
    # BEGIN Q3
        # Check if *n* has been lit up. If not, what do we do?
    # END Q3

def print_board():
    """
    Display the board.
    """
    print(''.join(["          " + ("@" if lights[n] else "-") for n in range(NUM_OF_LIGHTS)]))

def moles():
    """
    Randomly assigns a mole to pop up.
    """
    # Question 4: Mole Popping Up
    # BEGIN Q4
        # Make sure to use our *rd* instance.
    # END Q4

def whack_a_mole():
    """
    Game Start!
    """
    print("Welcome to Whack A Mole Lite! \nLet's start a game!\n\n")
    _continue = True
    while _continue:
        # Question 5: Lite Game Logic
        # BEGIN Q5
            # What are the processes for one round?
        # END Q5
        pass    # Delete this line
    print("End of game. Thanks for playing!")


whack_a_mole()
