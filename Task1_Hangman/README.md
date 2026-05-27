# 🎮 Task 1 — Hangman Game

> **CodeAlpha Python Internship | Task 1**

A fully-featured, terminal-based Hangman game built with clean Python. Features live hangman ASCII art, a scoring system, input validation, and a smooth game loop — all in a single well-structured file.

---

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [How to Run](#-how-to-run)
- [Gameplay](#-gameplay)
- [Code Architecture](#-code-architecture)
- [Concepts Used](#-concepts-used)

---

## ✨ Features

| Feature | Description |
|---|---|
| ASCII Art Gallows | 7-stage hangman that updates with every wrong guess |
| Live Word Display | Reveals correctly guessed letters in real time |
| Input Validation | Rejects non-alpha, multi-char, and duplicate inputs |
| Session Scoring | Tracks wins and losses across multiple rounds |
| Clean UI | Screen clears between turns for a polished feel |
| Replay System | Prompts the player to play again after each round |

---

## 📁 Project Structure

```
Task1_Hangman/
│
├── hangman.py       # Main game — all logic, UI, and entry point
└── README.md        # This file
```

---

## ⚙️ Requirements

- Python **3.10+** (uses `list[str]` and `set[str]` type hints)
- No third-party libraries — **standard library only**

---

## ▶️ How to Run

```bash
# Clone or navigate to the project directory
cd Task1_Hangman

# Run the game
python hangman.py
```

---

## 🕹️ Gameplay

```
==================================================
           🎮  HANGMAN  🎮
==================================================

   ┌────┐
   │    │
   O    │
  /│\   │
  /     │
        │
════════╧════

  Word  :  p _ t h _ n
  Wrong :  a, e, z
  Lives :  ❤️ ❤️ 🖤 🖤 🖤 🖤
  Tries :  4 / 6
==================================================

  Enter a letter: _
```

- Guess one letter per turn
- You get **6 wrong guesses** before you lose
- The gallows builds up with each incorrect letter
- Win by revealing the entire word before running out of lives

---

## 🏗️ Code Architecture

```
main()
 └── run_game(secret_word)
      ├── display_game_state()   → renders board, gallows, progress
      ├── get_player_guess()     → validated input loop
      └── returns True/False     → win/loss result

Helpers
 ├── display_word()             → builds "_  _  t  h  _  n" string
 ├── display_wrong_guesses()    → formats wrong letter set
 ├── clear_screen()             → cross-platform terminal clear
 └── play_again()               → prompts for replay
```

---

## 🧠 Concepts Used

- `random.choice()` — word selection
- `set` — O(1) lookup for guessed letters
- `while` loop — game loop and input validation
- `f-strings` — dynamic UI rendering
- `os.system()` — cross-platform screen clearing
- Type hints (`list[str]`, `set[str]`, `bool`) — clean, readable code
- Docstrings — full function documentation

---

*CodeAlpha Python Internship — Task 1*
