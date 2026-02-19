# Starter Code for Hangman Game Assignment
# 🎮 This file provides skeleton functions that students will fill in to
# build a complete Hangman game.  Follow the comments in each task.

import random

# ---------------------------------------------------------------------------
# Task 1: Word selection and helpers
# ---------------------------------------------------------------------------

def choose_word():
    """Return a random word from the predefined list."""
    words = ['python', 'hangman', 'challenge', 'programming', 'computer']
    return random.choice(words)


def display_progress(secret_word, guessed_letters):
    """Return the current progress string, e.g. "h _ n g m a n"."""
    return " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )

# ---------------------------------------------------------------------------
# Task 2: Game loop
# ---------------------------------------------------------------------------

def play_hangman():
    """Run the main game loop for Hangman."""
    secret_word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    while incorrect_guesses < max_incorrect and set(secret_word) != guessed_letters:
        print("\nWord:", display_progress(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower().strip()
        if not guess or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in secret_word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word. "
                  f"({max_incorrect - incorrect_guesses} guesses left)")

    if set(secret_word) <= guessed_letters:
        print(f"\nCongratulations! You guessed '{secret_word}'!")
    else:
        print(f"\nOut of guesses. The word was '{secret_word}'. Better luck next time!")

# ---------------------------------------------------------------------------
# Task 3: Entry point
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    play_hangman()
