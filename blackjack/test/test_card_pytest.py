import pytest
import unittest
from blackjack.card import BlackjackCard, NumberCard, FaceCard, AceCard
from card_factory import CardFactory


class BlackjackCardTest(unittest.TestCase):

    def test_blackjack_card(self):
        test = BlackjackCard(5, 1)
        assert test.rank == 5
        assert test.suit == 1
        assert str(test) == '5 of ♢'
        del test


class CardFactoryTest(unittest.TestCase):

    def test_number_card(self):
        test = CardFactory.create_card(5, 1)
        assert isinstance(test, NumberCard)
        assert test.rank == 5
        assert test.suit == 1
        assert test.soft_score == test.hard_score == test.rank
        assert str(test) == '5 of ♢'
        del test

    def test_ace_card(self):
        test = CardFactory.create_card(1, 2)
        assert isinstance(test, AceCard)
        assert test.rank == 1
        assert test.suit == 2
        assert test.soft_score == 1
        assert test.hard_score == 11
        assert str(test) == 'Ace of ♡'
        del test

    def test_face_card(self):
        test = CardFactory.create_card(11, 2)
        assert isinstance(test, FaceCard)
        assert test.rank == 11
        assert test.suit == 2
        assert test.soft_score == 10
        assert test.hard_score == 10
        assert str(test) == 'Jack of ♡'
        del test