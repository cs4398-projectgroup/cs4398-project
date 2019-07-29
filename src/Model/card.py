class Card:
    """
    Abstract base class for all cards in any deck

    Attributes:
        card_ranks (str): The 13 different cards contained in each suit
        card_suits (str): The four suits offered in a standard deck of playing cards

    Returns:
        description of return

    Raises:
        KeyError: exceptions it raises
    """

    card_suits = ["♣", "♢", "♡", "♠"]
    card_ranks = [
        None,
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = f"{Card.card_ranks[self.rank]} of {Card.card_suits[self.suit]}"
        self.visible = True

    def __str__(self) -> str:
        return self.name if self.visible else "<hidden>"

    def __eq__(self, other) -> bool:
        """

        Args:
            other (Card):
        """
        return other.rank == self.rank and self.suit == other.suit


class BlackjackCard(Card):
    """
    Super class for the cards in a Blackjack deck

    Args:
        rank (int):
        suit (int):

    Returns:
        description of return

    Raises:
        KeyError: exceptions it raises
    """

    def __init__(self, rank, suit):
        super().__init__(rank, suit)

    def __str__(self):
        return super(BlackjackCard, self).__str__()


class NumberCard(BlackjackCard):
    def __init__(self, rank, suit):
        super().__init__(rank, suit)
        self.soft_score = self.hard_score = rank


class AceCard(BlackjackCard):
    def __init__(self, rank, suit):
        super().__init__(rank, suit)
        self.soft_score, self.hard_score = 1, 11

    @staticmethod
    def soft_score() -> int:
        return 1

    @staticmethod
    def hard_score() -> int:
        return 11


class FaceCard(BlackjackCard):
    def __init__(self, rank, suit):
        super().__init__(rank, suit)
        self.soft_score = self.hard_score = 10