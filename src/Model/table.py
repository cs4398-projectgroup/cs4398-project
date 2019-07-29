from Model.player import BlackjackPlayer, BlackjackHand


class Table:
    pass


class BlackjackTable(Table):
    """
        Class for a Table object. The Table's life cycle consist of
        a single game of blackjack. The table will contain a Player,
        a Dealer, and the Bet (for the current game).

        Args:

        Returns:
             A Blackjack Table with a Blackjack Player, An initial Ante,
             and a Blackjack Dealer.

        Raises:
            KeyError: exceptions it raises
    """
    def __init__(self):
        self.player = BlackjackPlayer
        self.house = BlackjackHand

    def set_player(self, player):
        self.player = player

    def set_house(self, house):
        self.house = house

    def deal_player_hand(self):
        pass

    def deal_house_hand(self):
        pass
