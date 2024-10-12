<img align="right" src="https://github.com/pioneers/shepherd-onboarding/blob/master/readmefigures/PiE_Sheep.png" alt="PiE Sheep" width="86" height="135">

# Shepherd

Shepherd is the team that is in charge of field control. 
Shepherd brings together all the data on the game field into one centralized location, where it keeps track of score, processes game-specific actions, keeps track of time, and informs the scoreboard.

## Architecture

To read about Shepherd in detail, check out the [onboarding readme](https://github.com/pioneers/shepherd-onboarding#about-shepherd). This is where you will find detailed information about what each component of Shepherd does.



# Whack-A-Mole Lite

## Introduction
In this project, you will implement a simple version of "Whack-A-Mole" game. The game randomly lights up one of five positions, and the player must input the correct key to "whack" the mole. The game ends when the player misses a mole.

## How It Works
- The game board consists of 5 lights, represented by "@" (for a mole) and "-" (for an empty spot).
- A mole randomly appears at one of these 5 positions.
- The player uses the keyboard to whack the mole based on the corresponding position.

## Game Rules
- At the start of each round, a mole will appear in one of the positions.
- You have to "whack" the mole by pressing one of the following keys:
    - 'a' for position 0
    - 's' for position 1
    - 'd' for position 2
    - 'f' for position 3
    - 'g' for position 4
- If you press the correct key and there is a mole at that position, the mole disappears, and the game continues.
- If you press the wrong key, or there is no mole in that position, the game ends.
- The file you will be editing is `whack-a-mole-lite.py`.

## Functions
### Question 1-1: Set Up the "Board"
Initialize the lights list, which represents the board with a fixed number of lights (in this case, 5). Each light can either be `True` (indicating a mole is present) or `False` (no mole). The list initially indicates no moles are present at the start.

### Question 2-1: Treat Keyboard Input
The `keyboard_input()` function reads the player's input, processed through the wrapper function. Here, you need to check if the input (`line`) is a valid number corresponding to one of the lights (positions 0-4). If so, the `whack()` function is called with the corresponding position as an argument. This checks whether there is a mole to "whack" at the specified position.

### Question 3: Whack The Mole!
The `whack()` function attempts to "whack" the mole at position n. If there is no mole present, it prints `oops...` and returns `False`, indicating a failed attempt. If there is a mole, it turns off the light and returns `True` to show a successful whack.

### Question 4: Mole Popping Up
For the `moles()` function, you need to randomly select a position from the range of available lights (0 to 4) and set that position to `True`, indicating that a mole has appeared at that position. Hint: You can use `rd.randint()` to make random a choice ensuring randomness within the game.

### Question 5: Lite Game Logic
Within the main game loop of `whack_a_mole()`, a mole randomly pops up by calling the `moles()` function, the current state of the board is printed showing where moles are located and the game waits for user input via `keyboard_input()`. Based on the input, the player attempts to whack a mole.

## How to Play
1. Run the script.
2. Follow the instructions on the screen.
3. When a mole appears (represented by `@`), press the corresponding key ('a', 's', 'd', 'f', or 'g') to whack it.
4. The game continues until you miss a mole (i.e., press the wrong key or whack an empty spot).



