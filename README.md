Ghost Game
Overview

Ghost is a two-player word game implemented in Python. Players take turns adding a single letter to a growing word fragment, trying not to complete a valid word. The player who completes a valid word (of 4 or more letters) or creates a fragment that cannot form any word loses the game.

This version uses a dictionary file (words.txt) as the source of valid words.

Features

Two-player turn-based gameplay.

Real-time input validation for single alphabetic characters.

Automatic checks for valid words and playable fragments.

Switches turns automatically between players.

Requirements

Python 3.x

words.txt file containing a list of lowercase words (one per line).

Installation

Install Python from python.org
.

Ensure the words.txt file is in the same directory as ghost.py.

Open a terminal or PowerShell window.

Navigate to the folder containing ghost.py and words.txt:

cd path\to\your\folder

Usage

Run the game using Python:

python ghost.py

Gameplay Instructions:

The game starts with an empty word fragment.

Players alternate turns, adding one letter at a time.

The game continues until:

A player completes a valid word (≥ 4 letters) → that player loses.

A player creates a fragment that cannot start any word → that player loses.

Input must be a single alphabet letter; otherwise, the game prompts again.

Functions

load_words(): Loads a list of valid words from words.txt.

is_word(word): Returns True if a word exists in the dictionary.

can_form_word(fragment): Returns True if any word can be formed from the fragment.

ghost(): Main game loop handling input, turn-taking, and game logic.

Authors

Ntokoza Maselala – Game implementation

Jimmy Shabalala – Collaborator

License

This project is free to use for educational purposes.
