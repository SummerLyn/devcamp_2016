'''
Required:
card class
deck class
hand class
'''

class Card:
    ### setting a denomination card value that is a dictionary - assigns the key "face" a value: --- ie Jack:10...
    card_value = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        "Ace": 11
        }

    def __init__(self, suit, face):
        self.face = face
        self.suit = suit
        self.value = Card.card_value[face]
        self.is_hidden = False

    def __repr__(self):
        """ repr tells python how to print the card. """
        return "{} {}".format(self.face, self.suit)

    def ace_demote(self):
        if self.value == 11:
            self.value = 1
            print("Your Ace is now = 1 ")
