from cardclass import Card
from random import shuffle
from itertools import product

suits = ['\u2660', '\u2665', '\u2666', '\u2663']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


class Deck:

    def __init__(self, num_decks):
        self.num_decks = num_decks
        self.cards = []
        self.make_deck()

    # this is creating a deck out of suits and faces. Using 'product' for more efficient looping
    def make_deck(self):
        self.cards = []
        for deck in range(self.num_decks):
            for suit, face in product(suits, faces):
                self.cards.append(Card(suit, face))
            # populates each suit and face together into a list called cards
        shuffle(self.cards)

    # takes the dealt card out of deck
    def deal_card(self):
        return self.cards.pop()


class Player:

    def __init__(self, player_name):
        self.hand = []
        self.player_name = player_name
        self.score = 0
        self.status = False

    def player_input(self):
        """This functions allows the player to a choice to hit or stay"""
        player_decision = input("{}, Type 'h' to hit, or 's' to stay. >> ".format(player.player_name))
        if player_decision.lower() == "h":
            player.hand.append(self.deck.deal_card())
            player.print_hand()
            player.status = player.score_hand()
        else:
            player.status = True

        while player_decision == "":
            if player_decision != "h" or "s":
                print("That is not a valid option. Do you wish to hit or stay?")
                player_decision = ""
        return player_decision

    def score_hand(self):
        count = 0
        for card in self.hand:
            count += card.value
        if count > 21:
            for card in self.hand:
                if card.ace_demote():
                    break
            else:
                self.status = "Busted!"
                self.score = count
                return

        count = 0

        for card in self.hand:
                count += card.value
        self.score = count
        # if you got a blackjack, declare immediate victory
        if self.score == 21:
            self.status = "WINNER!"


class Dealer(Player):

        def __init__(self, dealer_name):
            # do all the setup for a usual Player object
            super().__init__(dealer_name)
            # overwrite showing to be False
            self.score = "xx"
            self.showing = False

        def dealer_decision(self):
            return self.score <= 17
