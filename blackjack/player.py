import sys
from abc import ABC, abstractmethod

from hand import BlackjackHand
from deck import Deck


class Player(ABC):
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
