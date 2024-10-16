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

# Whack A Mole - Advanced Edition

## Introduction
This version of "Whack A Mole" introduces an advanced, multithreaded game setup where moles appear on a board, and the user is required to hit the corresponding buttons to "whack" them. The game uses threading, a queue to handle user input, and integrates with an external device (via the ydl client) for button press and light management. For this section, you will be editing `whack_a_mole.py` file.

## How to Play
1. Lights: There are 3 lights (positions 0, 1, and 2), represented by buttons `a`, `s`, and `d` on the keyboard.
    - a: Whacks position 0.
    - s: Whacks position 1.
    - d: Whacks position 2.
2) Moles randomly appear in one of the 3 positions, and the player must press the corresponding button to whack the mole.
3) The game will display feedback:
    - "GOOD!": If you successfully whack the mole.
    - "oops...": If you press a button with no mole present.
The game ends when the player misses or presses a button in the wrong spot.

## File Structure
- `NUM_OF_LIGHTS`: The number of lights/buttons in the game (3 in this version).
- `rd`: A random generator to determine mole appearances.
- `lights`: A list of boolean values representing whether a mole is present at each position (`True` for a mole, `False` for no mole).
- `q`: A queue to handle user input asynchronously.
- `yc`: The client used to send events (button presses and light states) to an external system for feedback and control.

## Functions
### Question 1-2: Set Up the "Board"
Follow the hints from `whack-a-mole-lite.py`

### Question 2-2: Treat Keyboard Input
Follow the hints from `whack-a-mole-lite.py`. The `yc.send()` function is also used to send the button press event to the external client.

### Question 6: Whack The Mole...?
This function adds the player's input (the position of the whack) to the queue (`q`). This queue ensures that the input is processed in the correct order, and helps manage multiple inputs.

### Question 7-1: Turn On the Light
Turn on the light at position `n` by setting `lights[n]` to `True` and sending the appropriate event (`TURN_ON_BUTTON_LIGHT`) to the external client, indicating that a mole has appeared at that position.

### Question 7-2: Turn Off the Light
This function turns off the light at position `n` by setting `lights[n]` to `False` and sends the `TURN_OFF_BUTTON_LIGHT` event to the external client, indicating that the mole has been whacked or has disappeared.

### Question 8: Mole Popping Up
Randomly turn on a light (i.e., makes a mole appear) by selecting a random position using the random generator (`rd`) and calling `turn_on()` for that position.

### Question 9: Activate Mole
The game logic randomly activates a mole by calling the `moles()` function. This function handles turning on a random light, making it ready for the player to whack.

### Question 10: Trial to Pull Keyboard Input
Here, the function attempts to pull the player's input from the queue using `q.get()`. If the queue is empty, it raises a `queue.Empty` exception, and the loop continues until an input is available.

### Question 11: Whacking Logic
This logic checks if there is a mole at position `n`. If there is no mole (`lights[n] == False`), it prints "oops...", turns on the light (to indicate an error), and raises a `StopIteration` exception to stop the game. If there is a mole, it turns off the light, prints "GOOD!", and continues the game.

### Question 12: End of Game
At the end of the game, this code turns off all the lights by calling `turn_off()` for each position in the `lights` list that is currently `True`. This ensures that all the lights are turned off before the game ends.

## Running the Game
Ensure the following requirements are met:

1. The external client (ydl and associated targets like SHEPHERD) are set up and running.
2. Run the script, and the game will begin immediately.
3. Input commands (a, s, d) correspond to the respective button presses.
The game loop will run until the player fails to hit the correct mole.

Congratulations! You are two thirds of the way. baa! 

# Whack A Mole - Client and Handler

## Introduction
Now, you will edit the last part for Whack A Mole game in `board.py`. This module acts as a client and handler integrating with an external device to manage button lights that represent moles in the game. 

## File Structure 
- `Client`: An instance of `Client` from the `ydl` library that connects to the external system (SHEPHERD).
- `Handler`: An instance of `Handler` that listens for specific events to manage the button lights.

## Functions
### Question 1-3: Set Up the "Board"
Follow the instructions from before.

### Question 7-3: Turn On the Light
This function is triggered when a light should be turned on. It updates the `lights` list by setting the value at index `id` to `True`, indicating that the light is now on (a mole is present). This function is registered to respond to the `SHEPHERD_HEADER.TURN_ON_BUTTON_LIGHT` event.

### Question 7-4: Turn Off the Light
This function is called when a light should be turned off. It updates the `lights` list by setting the value at index `id` to `False`, indicating that the light is now off (no mole is present). This function responds to the `SHEPHERD_HEADER.TURN_OFF_BUTTON_LIGHT` event.

## The End