import unittest
import pytest

from Control.deck import Deck


class DeckTest(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_number_of_cards(self):
        self.assertEqual(len(self.deck._cards), 52)

    def test_draw_deck(self):
        self.deck.draw()
        self.assertEqual(len(self.deck._cards), 51)

    def test_draw_card(self):
        test_card = self.deck.draw()
        self.assertNotIn(test_card, [c for c in self.deck._cards])


if __name__ == "__main__":
    unittest.main()
