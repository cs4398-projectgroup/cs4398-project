from Model.deck import Deck
from Control.dealer import Dealer
from Control.player import Player


class BlackjackController(object):
    """"Calculates and keeps track of the game, points, deck"""

    def __init__(self):
        self.currentDeck = Deck()
        self.currentDeck.shuffle()

        """Deal player and dealer 2 cards each"""
        self.currentPlayer = Player([self.currentDeck.deal(), self.currentDeck.deal()])
        self.currentDealer = Dealer([self.currentDeck.deal(), self.currentDeck.deal()])

    def get_players_hand(self):
        """Returns player's hand"""
        return self.currentPlayer.get_hand()

    def get_dealers_hand(self):
        """Returns dealer's hand"""
        return self.currentDealer.get_hand()

    def hit_player(self):
        card = self.currentDeck.deal()
        card.turn()
        self.currentPlayer.hit(card)
        # Returns tuple of the card and total points
        return (card, self.currentPlayer.get_score())

    def hit_dealer(self):
        """Dealer only hits after the player stands"""
        self.currentDealer.show_first_card()
        player_score = self.currentPlayer.get_score()
        if player_score > 21:
            return "You bust and lose!"
        else:
            self.currentDealer.hit(self.currentDeck)
            dealer_score = self.currentDealer.get_score()
            if dealer_score > 21:
                return "Dealer busts! You win!"
            elif player_score > dealer_score:
                return "You win!"
            elif player_score < dealer_score:
                return "You lose!"
            elif player_score == dealer_score:
                if (
                    self.currentPlayer.has_blackjack()
                    and not self.currentDealer.has_blackjack()
                ):
                    return "You have a BlackJack! You Win!"
                elif (
                    not self.currentPlayer.has_blackjack()
                    and self.currentDealer.has_blackjack()
                ):
                    return "Dealer has a BlackJack! You Lose!"
                else:
                    return "It's a Tie!"
