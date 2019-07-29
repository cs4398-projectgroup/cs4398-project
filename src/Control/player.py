import sys

from Control.hand import BlackjackHand
from Control.deck import Deck


class Player:
    """
    Abstract base class for all players at a table

    Args:
        param1:

    Returns:
        description of return

    Raises:
        KeyError: exceptions it raises
    """
    pass


class BlackjackPlayer(Player):
    """
    Superclass for a blackjack player

    Args:
        hand (Hand): The initial hand of blackjack player

    Returns:
        description of return

    Raises:
        KeyError: exceptions it raises
    """

    def __init__(self, name: str):
        self.name = name

    def ask_to_hit(self) -> bool:
        answer = input("Hit? (Y/N): ")
        if answer == 'Y' or 'y':
            return True
        else:
            return False

    def bust(self):
        print(self.name, "bust")
        self.lose()

    def lose(self):
        print(self.name, "loses")

    def win(self):
        print(self.name, "wins")


class BlackjackHouse(Player):
    def __init__(self, hand=None):
        self.hand = BlackjackHand("House")

    def set_hand(self, new_hand):
        self.hand = new_hand

    def house_hit(self, hand) -> bool:
        if self.hand.hard_total() < 17:
            return True
        else:
            return False

