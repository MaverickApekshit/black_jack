'''
Text based Black Jack game
'''

#To shuful the deck
import random


#Global variables to create the deck of cards
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
         'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
          'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


#Boolean to control the flow of game
PLAYING = True


class Card():
    """Class for card object"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        '''Method to print a Card'''

        return self.rank + " of " + self.suit


class Deck():
    """Store 52 card objects in a list (deck) that can later be shuffled"""

    def __init__(self):
        self.deck = [] # Start with an empty list
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        '''Method to print the deck. May only be used for debugging'''

        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        '''Method to shuffle the deck'''

        random.shuffle(self.deck)

    def deal(self):
        '''Method to deal the card'''

        single_card = self.deck.pop()
        return single_card

class Hand():
    """Class for Hand that has been delt"""

    def __init__(self):
        self.cards = [] # Hand starts empty
        self.value = 0  # Start value is 0
        self.aces = 0   # Attribute to keep track of aces

    def add_card(self, card):
        '''card passed in from Deck.deal() --> single Card(suit, rank)'''

        self.cards.append(card)
        self.value += VALUES[card.rank]
