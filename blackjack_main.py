# blackjack_main.py

"""
Milestone Project 2 - Blackjack Game 

In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:
You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the players total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:
You must use OOP and classes in some portion of your game. 
You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. 
There are many right ways to do this, so explore it well!
Feel free to expand this game-try including multiple players. 
Try adding in Double-Down and card splits! 

Remember to you are free to use any resources you want and as always: HAVE FUN!
"""


class Deck(object):
    cards = ['2 C', '3 C', '4 C', '5 C', '6 C', '7 C', '8 C', '9 C', '10 C', 'J C', 'Q C', 'K C', 'A C',
             '2 H', '3 H', '4 H', '5 H', '6 H', '7 H', '8 H', '9 H', '10 H', 'J H', 'Q H', 'K H', 'A H',
             '2 D', '3 D', '4 D', '5 D', '6 D', '7 D', '8 D', '9 D', '10 D', 'J D', 'Q D', 'K D', 'A D',
             '2 S', '3 S', '4 S', '5 S', '6 S', '7 S', '8 S', '9 S', '10 S', 'J S', 'Q S', 'K S', 'A S']

    def shuffle_deck(self):
        from random import shuffle
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)

    def reset_deck(self):
        pass


class DisplayBoard(object):
    def display_DealerHand(self):
        pass

    def displayPlayerHand(self):
        pass

    def display_player_bank(self):
        pass

    def display_player_bet(self):
        pass


class Hand(object):
    hand_value = 0

    def deal_hand(self, deck):
        for i in [0, 1]:
            card = deck.deal_card()
            print card

    def set_hand_value(self, card):
        if str(card).endswith('A'):
            pass

    def calculate_hand_value(self, cards):
        pass


class Player(object):
    def __init__(self):
        pass

    def place_a_bet(self):
        pass

    def stand(self):
        pass

    def hit(self):
        pass


my_deck = Deck()
my_deck.shuffle_deck()
print my_deck.cards

# for i in my_deck.cards:
#     print i


my_hand = Hand()
print ' HAND'
my_hand.deal_hand(my_deck)

print my_deck.cards
