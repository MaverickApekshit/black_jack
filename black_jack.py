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

    def adjust_for_ace(self):
        '''Adjust the ace value to be 11 or 1 based on the Hand value'''

        while (self.value > 21) and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    """Class to keep track of Player's chips/money"""

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        '''If player wins the bet, add to the total chips'''

        self.total += self.bet

    def lose_bet(self):
        '''If player looses the bet, subtract from the total'''

        self.total -= self.bet

def take_bet(chips):
    '''Function to take bets from the player'''

    while  True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have: {chips.total}')
            else:
                break

def hit(deck, hand):
    '''Function to perform a hit'''

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    '''Function to check if the player wants to Hit or Stand'''

    global PLAYING   #to control an upcoming while loop

    while True:
        x = input('Hit or Stand? Enter h or s')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands, Dealer's Turn")
            PLAYING = False

        else:
            print("Sorry, I did not understand that. Please enter h or s only!")
            continue

        break

def show_some(player,dealer):
    '''Function to show all cards, except Dealer's first card.'''

    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    '''Function to show all cards'''

    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


'''
Endgame Scenarios
'''
def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player, dealer, chips):
    print("Dealer and player tie! PUSH")
