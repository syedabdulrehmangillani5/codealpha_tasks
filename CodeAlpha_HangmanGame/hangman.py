"""
CodeAlpha Python Internship - Task 1: Hangman Game
Author: Your Name
Description: A text-based Hangman game. The player guesses a randomly
             chosen word one letter at a time, with a maximum of 6
             incorrect guesses.
"""

import random

WORDS = ["python", "internship", "program", "keyboard", "developer"]
MAX_WRONG_GUESSES = 6


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def get_guess(guessed_letters):
    """Ask the player for a valid, new single-letter guess."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def play_game():
    """Run one round of Hangman."""
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("\n=== Welcome to Hangman! ===")
    print(f"The word has {len(word)} letters. You can make {MAX_WRONG_GUESSES} wrong guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) or "none")

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations, you won! The word was '{word}'.")
            return

    print(f"\nGame over! You ran out of guesses. The word was '{word}'.")


def main():
    """Play rounds until the player decides to stop."""
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
