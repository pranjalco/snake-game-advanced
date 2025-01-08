# Project 15: Snake Game

## Author
- **Name**: Pranjal Sarnaik
- **Date**: 2024-12-21

## Description:
The Snake Game is an advanced Python project implemented using OOP principles. It uses the `turtle`, `random`, and `time` modules to provide an interactive and engaging gameplay experience. The game includes a moving snake, food for the snake to consume, and a scoreboard that tracks the current score and high score. The high score is saved in a `high_score.txt` file within the project folder, ensuring persistence across sessions.

## How to Use:
1. Use the arrow keys to control the snake's movement.
2. The objective is to eat the food while avoiding collisions with the walls or the snake's tail.
3. The score increases as the snake consumes food. The high score is updated and saved automatically.

## Level
- **Level**: Advanced
- **Skills**: OOP, File Handling, Collision Detection, Turtle Graphics
- **Domain**: Game Development

## Features
- Object-Oriented Programming with separate classes:
  - **Snake Class** (`snake.py`): Handles snake creation, movement, direction changes, extending the snake, and resetting its position.
  - **Food Class** (`food.py`): Manages food placement and appearance.
  - **Scoreboard Class** (`scoreboard.py`): Manages score updates, high score tracking, and screen display.
- High score tracking:
  - Fetches and saves the high score in `high_score.txt`.
  - Updates the file whenever a new high score is achieved.
- Collision detection:
  - With food: Snake grows, and score increases.
  - With walls: Game resets, and high score is preserved.
  - With tail: Game resets, and high score is preserved.
- Experiments folder:
  - Contains temporary files or practice code used during development.
- Modified on: 2024-12-21 (additional features added later).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pranjalco/snake-game-advanced.git
   ```

2. Navigate to the project directory:
   ```bash
   cd snake-game-advanced
   ```

## Running the Program
1. Ensure Python 3.9 or later is installed on your system.
2. To run the program:
   - **Using PyCharm**: Open the project in PyCharm and run `app.py`.
   - **Using Terminal/Command Prompt**: Navigate to the project folder and execute:
     ```bash
     python app.py
     ```
   - **By Double-Clicking**: You can double-click `app.py` to run it directly, provided Python is set up to execute `.py` files on your system.
3. If the console window closes immediately, run the program from the terminal/command prompt or IDE to see the output.

---
**Created by Pranjal Sarnaik**  
*© 2024. All rights reserved.*

