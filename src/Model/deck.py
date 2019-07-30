from src.Model.card import Card
import random


class Deck(object):

    def __init__(self):
        """Creates a full deck of cards. suits * rank = 52"""
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.deck.append(c)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)

    def __str__(self):
        """Returns the string representation of the deck"""
        self.cards_in_the_deck = ''
        for card in self.deck:
            self.cards_in_the_deck = self.cards_in_the_deck + str(card) + '\n'
        return self.cards_in_the_deck

    def __len__(self):
        """Returns the number of cards in the deck"""
        return len(self.deck)