# Flappy Bird Game - README

## Overview

This project is a Python implementation of the classic Flappy Bird game using the Pygame library. The game involves controlling a bird to fly through gaps between pipes without hitting them. The player scores points by successfully navigating through the pipes.

## Features

- Animated bird with flapping wings
- Randomly generated pipes
- Scrolling ground
- Score tracking and high score persistence
- Restart and quit buttons
- "Game Over" animation
- Sound effects for success and failure

## Requirements

- Python 3.x
- Pygame library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/flappy-bird.git
    cd flappy-bird
    ```

2. **Install Pygame:**

    ```bash
    pip install pygame
    ```

## Running the Game

Navigate to the project directory and run the main script:

```bash
python main.py
```

## Game Controls

- **Mouse Click:** Make the bird jump.
- **Restart Button:** Restart the game after a game over.
- **Quit Button:** Exit the game.

## Project Structure

- `main.py`: Main script containing the game logic and functions.
- `images/`: Directory containing all image assets (background, bird, pipes, buttons, letters).
- `sounds/`: Directory containing all sound effects (success, failure, game over).
- `score.txt`: File for storing the high score.

## Detailed Description

### Images

- **Background Image**: `images/bg.png`
- **Ground Image**: `images/ground.png`
- **Restart Button Image**: `images/restart.png`
- **Exit Button Image**: `images/exit.png`
- **Bird Images**: `images/bird1.png`, `images/bird2.png`, `images/bird3.png`
- **Pipe Image**: `images/pipe.png`
- **Game Over Letters**: `images/G.png`, `images/A.png`, `images/M.png`, `images/E.png`, `images/O.png`, `images/V.png`, `images/R.png`
- **Press to Start Image**: `images/press.png`

### Sounds

- **Success Sound**: `sounds/success.wav`
- **Failure Sound**: `sounds/fall.wav`
- **Game Over Sound**: `sounds/game_over.mp3`

### Game Variables

- **Ground Scroll**: Controls the movement of the ground.
- **Scroll Speed**: Speed at which the ground and pipes move.
- **Flying**: Boolean flag to check if the bird is in the air.
- **Game Over**: Boolean flag to check if the game is over.
- **Pipe Gap**: Gap between the top and bottom pipes.
- **Pipe Frequency**: Time interval for generating new pipes.
- **Score**: Player's current score.
- **Tries**: Number of lives remaining.
- **Letter Speed**: Speed of the "Game Over" animation.
- **Speed Counter**: Counter to control the animation speed.

### Functions

- **draw_text**: Draws text on the screen.
- **check_score**: Checks and updates the score.
- **_pass**: Handles the passing of pipes and score increment.
- **check_collision**: Checks for collisions between the bird and pipes or the top of the screen.
- **check_scroll**: Handles the scrolling of the ground.
- **hit_ground**: Checks if the bird has hit the ground.
- **Game_Over**: Manages the game over state and animations.
- **new_live**: Resets the game state for a new try.
- **reset_game**: Resets the entire game state.
- **quit_game**: Quits the game.
- **lives**: Displays the remaining lives.

### Classes

- **Bird**: Represents the bird with animation and movement.
- **Pipe**: Represents the pipes.
- **Button**: Represents the restart and quit buttons.
- **Letter**: Represents the letters of the "Game Over" text.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Pygame community for the excellent library and resources.
- Inspiration from the original Flappy Bird game.
