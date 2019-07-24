from hand import Hand
from player import BlackjackPlayer, BlackjackHand


class Table:
    pass


class BlackjackTable(Table):
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

    def check_bust(self):
        pass

    def check_blackjack(self):
        pass

    def check_winner(self):
        pass


