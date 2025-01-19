#  9.7 Write a program to pick a random card from a standard deck of 52 cards

import random

def pick_random_card():
    """Function to pick a random card from a standard 52-card deck."""
    # Define the suits and ranks
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    # Combine ranks and suits to form a deck
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    
    # Pick a random card from the deck
    random_card = random.choice(deck)
    
    return random_card

# Pick and display a random card
print("Randomly picked card:", pick_random_card())
