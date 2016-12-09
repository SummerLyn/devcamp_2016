from Cardclass import Card
from random import shuffle
from itertools import product

class Deck:

    def __init__(self):
        self.cards = []
        self.make_deck()

    def make_deck(self):
        suits = ['\u2660', '\u2665', '\u2666', '\u2663']
        faces = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        for suit, face in product(suits, faces):
            # this is creating a deck out of suits and faces. Using 'product' for more efficient looping
            self.cards.append(Card(suit, face))
            # populates each suit and face together into a list called cards
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
