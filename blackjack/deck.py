from random import shuffle

from card_factory import CardFactory


class Deck:
    """
        Class for a standard 52 deck of playing cards. Defines
        A deck so the internal collection is a list object

        Args:

        Returns:
            The top card of the deck.

        Raises:
            KeyError: exceptions it raises
    """

    def __init__(self):
        card_factory = CardFactory()
        self._cards = [
            card_factory.create_card(rank + 1, suit)
            for rank in range(0, 13)
            for suit in range(4)
        ]
        shuffle(self._cards)

    def __len__(self):
        return len(self._cards)

    def __iter__(self):
        return iter(self._cards)

    def draw(self, amount: int):
        if amount == 1:
            return self._cards.pop()
        return [self._cards.pop() for cards in range(0, amount)]
