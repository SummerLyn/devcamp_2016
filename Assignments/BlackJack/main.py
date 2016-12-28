from deckclass import *


class Main:

    def __init__(self, num_players, num_decks):
        self.num_players = num_players
        self.players = []
        self.deck = Deck(num_decks)
        self.dealer = Dealer("Dealer")
        #self.start_game()
        for x in range(num_players):
            name = input(" What is Player {}'s name? >> ".format(x + 1))
            self.players.append(Player(name))


        #this function determines number of players, deals cards, and starts turn
    def start_game(self):
        still_playing = True

        while still_playing:
            # this deals 2 cards into hand
            for player in self.players:
                player.hand.append(self.deck.deal_card())
                player.hand.append(self.deck.deal_card())
                print("\n {} , these are your cards: {}.".format(player.player_name, player.hand))
                player.status = player.score_hand()
                if player.score == 21:
                    print("\m BlackJack, {}! You got lucky. ".format(player.player_name))
                elif player.score > 21:
                    print("\n Ha! You've busted, {}! The House WINS!".format(player.player_name))
                self.dealer.hand.append(self.deck.deal_card())
                self.dealer.hand.append(self.deck.deal_card())
                print("\n Dealer is showing: {}, {}".format('\U0001F0A0', self.dealer.hand[1]))

                self.dealer.status = self.dealer.score_hand()

            # this loop gives each player a full turn
            for player in self.players:
                print("\n Your turn, {}. You've got, {}".format(player.player_name, player.hand))
                while player.status == "":
                    self.player_input(player)
                    if player.score == 21:
                        print("Blackjack for you, {}.".format(player.player_name))
                    elif player.score > 21:
                        print("You've busted, {}! The House wins again! ".format(player.player_name))

            #while self.dealer.status == False:
               # self.turn(self.dealer)



            for player in self.players:
                self.determine_winner(player)

            still_playing = self.play_again()

    # Compare value of players hand and then determine winner.
    def determine_winner(self, player):

        if player.score == 21:
            print(" You've won, {}. Don't let it go to your head.".format(player.player_name))
        elif player.score > 21:
            print(" You've busted, {}. Your cash is mine! ".format(player.player_name))
        else:
            if player.score > self.dealer.score:
                print(" You beat me, {}. This displeases me.".format(player.player_name))
            elif self.dealer.score > 21:
                print(" I've gone over, {}. ".format(player.player_name))
            else:
                print(" You lost, {}. Get used to it. ".format(player.player_name))

    # resets the game
    def play_again(self):

        for player in self.players:
            player.hand = []
            player.score = 0
            player.status = False
            self.dealer.hand = []
            self.dealer.score = "xx"
            self.dealer.status = False


if __name__ == '__main__':
    print(" Let's play some BlackJack!")
    num_players = int(input("How many human players? >> "))
    num_decks = int(input("How many decks would you like to play with? >> "))
    game = Main(num_players, num_decks)
    game.start_game()
