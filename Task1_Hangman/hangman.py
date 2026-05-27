"""
Task 1 — Hangman Game
CodeAlpha Python Programming Internship

A terminal-based Hangman game with 7-stage ASCII art gallows,
session scoring, input validation, and replay support.
"""

import os
import random

# ── Constants ──────────────────────────────────
WORDS: list[str] = ["python", "engineer", "quantum", "voltage", "circuit",
                     "algorithm", "database", "function", "variable", "network"]

MAX_WRONG: int = 6

STAGES: list[str] = [
    """
   -----
   |   |
       |
       |
       |
       |
   ==========""",
    """
   -----
   |   |
   O   |
       |
       |
       |
   ==========""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
   ==========""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
   ==========""",
    """
   -----
   |   |
   O   |
  /|\\  |
       |
       |
   ==========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
   ==========""",
    """
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
   ==========""",
]


def clear_screen() -> None:
    """Clear the terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def display_word(secret_word: str, guessed: set[str]) -> str:
    """Build the display string showing guessed letters and blanks.

    Args:
        secret_word: The word to guess.
        guessed: Set of correctly guessed letters.

    Returns:
        A string like 'p _ t h _ n'.
    """
    return " ".join(letter if letter in guessed else "_" for letter in secret_word)


def display_wrong_guesses(wrong: set[str]) -> str:
    """Format the set of wrong guesses for display.

    Args:
        wrong: Set of incorrectly guessed letters.

    Returns:
        A comma-separated string of wrong letters.
    """
    return ", ".join(sorted(wrong)) if wrong else "None"


def get_player_guess(guessed: set[str], wrong: set[str]) -> str:
    """Prompt the player for a valid single-letter guess.

    Loops until the player enters a single alphabetic character
    that has not been guessed before.

    Args:
        guessed: Set of correctly guessed letters.
        wrong: Set of incorrectly guessed letters.

    Returns:
        A single lowercase letter.
    """
    while True:
        guess: str = input("\n Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter.")
            continue

        if guess in guessed or guess in wrong:
            print(f" You already guessed '{guess}'. Try another.")
            continue

        return guess


def display_game_state(secret_word: str, guessed: set[str], wrong: set[str]) -> None:
    """Render the full game board: gallows, word progress, and stats.

    Args:
        secret_word: The word to guess.
        guessed: Set of correctly guessed letters.
        wrong: Set of incorrectly guessed letters.
    """
    print(STAGES[len(wrong)])
    word_display: str = display_word(secret_word, guessed)
    wrong_display: str = display_wrong_guesses(wrong)
    lives_left: int = MAX_WRONG - len(wrong)

    print(f"\n  Word  : {word_display}")
    print(f"  Wrong : {wrong_display}")
    print(f"  Lives : {lives_left} / {MAX_WRONG}")


def run_game(secret_word: str) -> bool:
    """Run a single round of Hangman.

    Args:
        secret_word: The word the player must guess.

    Returns:
        True if the player won, False if they lost.
    """
    guessed: set[str] = set()
    wrong: set[str] = set()

    print(f"\n The word has {len(secret_word)} letters.\n")

    while len(wrong) < MAX_WRONG:
        clear_screen()
        print("=" * 50)
        print("            HANGMAN")
        print("=" * 50)

        display_game_state(secret_word, guessed, wrong)

        # Check win condition
        if all(letter in guessed for letter in secret_word):
            print(f"\n You won! The word was: {secret_word}")
            return True

        guess: str = get_player_guess(guessed, wrong)

        if guess in secret_word:
            guessed.add(guess)
            print(f" '{guess}' is in the word!")
        else:
            wrong.add(guess)
            print(f" '{guess}' is NOT in the word!")

    # Player lost — show final state
    clear_screen()
    print(STAGES[MAX_WRONG])
    print(f"\n Game Over! The word was: {secret_word}")
    return False


def play_again() -> bool:
    """Ask the player if they want to play another round.

    Returns:
        True if the player wants to play again, False otherwise.
    """
    answer: str = input("\n Play again? (y/n): ").lower().strip()
    return answer == "y"


def main() -> None:
    """Entry point: runs the Hangman game loop with session scoring."""
    wins: int = 0
    losses: int = 0

    while True:
        secret_word: str = random.choice(WORDS)
        result: bool = run_game(secret_word)

        if result:
            wins += 1
        else:
            losses += 1

        print(f"\n Score — Wins: {wins} | Losses: {losses}")

        if not play_again():
            print("\n Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Interrupted. Thanks for playing!")
