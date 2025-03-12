# Number Guessing Game

This is a simple Python-based number guessing game where the player attempts to guess a randomly generated number between 1 and 200.

## How the Code Works

1. **`intro()` function**
   - Prompts the player to enter their name.
   - Displays a message explaining the game rules.

2. **`runner()` function** (Game Logic)
   - Generates a random number between 1 and 200.
   - The player gets **6 attempts** to guess the correct number.
   - Checks if the guess is **out of range** (1-200).
   - Compares the guess with the generated number:
     - If **too low**, prompts the player.
     - If **too high**, prompts the player.
     - If correct, **congratulates the player** and ends the game.
   - Handles invalid inputs (non-numeric entries).
   - If the player **fails after 6 attempts**, the game reveals the correct number.

3. **`control_game()` function** (Game Flow)
   - Calls `intro()` to get the player's name.
   - Runs `runner()` inside a loop to allow replays.
   - Asks if the player wants to **play again**.
   - Ends the game with a farewell message if the player chooses not to continue.

4. **Game Start (`control_game()`)**
   - The game automatically starts when the script runs.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/number-guessing-game.git
   ```
2. Navigate to the project directory:
   ```sh
   cd number-guessing-game
   ```
3. Run the game:
   ```sh
   python guessing_game.py
   ```

## Files
- `number_guessing_game.py`: Main Python script containing the game logic.
- `README.md`: Documentation for the project.
