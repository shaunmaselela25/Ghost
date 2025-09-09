# Problem Set 5: Ghost
# Name: Ntokoza Maselala
# Collaborators: Jimmy Shabalala
# Date: September 2025
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')  # <-- removed the third argument
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

def is_word(word):
    """
    Returns True if word is in wordlist.
    """
    return word in wordlist
def can_form_word(fragment):
    """ 
    Returns True if there is any word in wordlist that starts with fragment.
    """ 
    for word in wordlist:
        if word.startswith(fragment):
            return True
    return False

def ghost(): 
    print("Welcome to Ghost!")
    fragment = ""
    player_turn = 0  # 0 for Player 1, 1 for Player 2
    while True:
        print(f"Current fragment: '{fragment}'")
        print(f"Player {player_turn + 1}'s turn.")
        letter = input("Please enter a letter: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Please enter a single alphabetic character.")
            continue
        
        fragment += letter
        
        if len(fragment) >= 4 and is_word(fragment):
            print(f"'{fragment}' is a word! Player {player_turn + 1} loses!")
            break
        
        if not can_form_word(fragment):
            print(f"No words can be formed with the fragment '{fragment}'. Player {player_turn + 1} loses!")
            break
        
        player_turn = 1 - player_turn  # Switch turns

ghost()
