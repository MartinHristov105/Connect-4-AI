# Connect Four AI

A graphical implementation of the classic **Connect Four** game built with **Python and Pygame**, featuring an AI opponent powered by the **Minimax algorithm with Alpha-Beta pruning**.

This project demonstrates game logic design, heuristic evaluation, and adversarial search algorithms.

---

## Features

- 10x10 game board
- Player vs AI gameplay
- Win detection:
  - Horizontal
  - Vertical
  - Diagonal (both directions)
- AI using:
  - Minimax algorithm
  - Alpha-Beta pruning optimization
  - Heuristic position evaluation
- Adjustable AI difficulty (search depth)

---

## Screenshots

![Start of the game](screenshots/start.png)
![Mid of the game](screenshots/mid.png)
![End of the game](screenshots/end.png)

---

## AI Implementation

The AI decision-making is based on:

### Minimax Algorithm
A recursive adversarial search algorithm that simulates future game states and selects the optimal move.

### Alpha-Beta Pruning
Optimization technique that reduces the number of evaluated nodes in the search tree, improving performance.

### Heuristic Evaluation Function
The evaluation function scores board positions based on:
- 4 in a row (winning positions)
- 3 in a row with open space
- 2 in a row with potential expansion
- Blocking opponent threats
- Center column control priority

---

## Technologies Used

- Python 3
- Pygame
- NumPy
- Object-oriented programming principles
- Recursive algorithms
- Game state evaluation techniques

---

## Installation

### Clone the repository

### Navigate into the project directory

### Create a virtual environment

### Activate the virtual environment

### Install dependencies

### Run the game 
 - python -m src.game	

--- 

## Adjusting AI Difficulty

- The AI difficulty is controlled by the search depth parameter
- PLAYER_VS_AI(4)
- Higher depth → stronger AI but slower computation.

---

## Project Structure

Project/
├── screenshots/
│   ├── gameplay.png
│   └── ai_win.png
├── src/
│   ├── constants.py
│   ├── game.py
│   └── utils.py
├── requirements.txt
├── .gitignore
└── README.md

---

## Learning Outcomes

This project demonstrates:

- Implementation of adversarial search algorithms
- Alpha-Beta pruning optimization
- Recursive problem solving
- Heuristic scoring systems
- Game loop architecture
- Event-driven programming with Pygame
- Clean project structuring for version control

---

## Future Improvements

- Adjustable board size
- Difficulty selection menu
- Performance optimization
- AI vs AI mode
- Refactoring into fully modular OOP structure

---

## Author
- Martin Hristov - https://github.com/MartinHristov105
- Yasen Uzunov - https://github.com/AJTheClear