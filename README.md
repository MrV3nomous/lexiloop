# Lexiloop 🎯

Lexiloop is a terminal-based word-chain game where players compete against each other or a smart AI. Players take turns forming words that start with the last letter of the previous word. The game is modular, fast, and designed to be engaging in a terminal environment like Termux or standard Python consoles.


----


## Features ✨

✔️ Single Player vs AI – Challenge a smart AI that balances strategy and variation.

✔️ Two Player Mode – Play with a friend on the same device.

✔️ Animated AI Thinking – AI moves are accompanied by a continuous spinner animation.

✔️ Input Validation – Ensures words are valid, not repeated, and follow the last-letter rule.

✔️ Quit Anytime – Players can type quit to give up.

✔️ Clean Terminal UI – Color-coded messages for easy readability.

✔️ Fast Gameplay – Optimized for speed even with large word datasets.

✔️ Modular Design – Code is split into game.py, player.py, utils.py, and word datasets for maintainability.



---



## Installation ⚡

### Clone the repository:

```bash
git clone https://github.com/MrV3nomous/lexiloop.git
cd lexiloop
```

### Install the required Python package:

```bash
pip install rich
```

### Run the game:
```bash
python main.py
```


---



## How to Play 🎮

- Choose Single Player or Two Player mode.
- A starting word is displayed.
- Enter a word that starts with the last letter of the previous word.
- Continue until a player cannot form a valid word or types quit.
- In single-player mode, the AI responds with a smart move while showing a spinner animation.



---



## Project Structure 📁

- datasets/words.txt – Word list for the game.
- player.py – Handles human and AI player logic.
- game.py – Main game loop and turn management.
- utils.py – Utility functions for color, delay, and printing.
- main.py – Entry point for the game.
- requirements.txt – Lists Python dependencies.



---



## License 📝
This project is licensed under the MIT License – see the LICENSE file for details.




