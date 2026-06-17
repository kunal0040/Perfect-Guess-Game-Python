# 🎯 Perfect Guess Game

An interactive, command-line number guessing game built in Python. The computer selects a secret number, and the player must deduce it. The game tracks the total number of attempts and records the all-time lowest score using local file storage.

## 🚀 Features
* **Adaptive Hints:** Tells the player if their guess is "Too high" or "Too low", with a special "Getting close!" warning if they are within 3 numbers of the target.
* **Robust Error Handling:** Uses `try-except` blocks to catch non-integer inputs gracefully, preventing the game from crashing if a user types a letter by mistake.
* **Persistent High Scores:** Implements file input/output (`open()`) to save and read the lowest number of guesses from a local `score.txt` file across different game sessions.

## 🛠️ Concepts Practiced
* **Exception Handling:** Managing runtime errors using `try` and `except ValueError`.
* **File Management:** Reading (`"r"`) and writing (`"w"`) to external text files.
* **Absolute Mathematics:** Using `abs()` to compute mathematical proximity regardless of whether a guess is higher or lower than the target.

## 📦 How to Run
1. Ensure you have Python installed.
2. Run the script using your terminal:
   ```bash
   python main.py