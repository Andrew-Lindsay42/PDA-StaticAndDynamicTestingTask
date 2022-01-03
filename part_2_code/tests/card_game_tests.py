import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.ace = Card('Spades', 1)
        self.nine = Card('Hearts', 9)
        self.five = Card('Diamonds', 5)
        self.hand = [self.ace, self.nine, self.five]
    
    def test_check_for_ace_true(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.ace))

    def test_check_for_ace_false(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.five))

    def test_highest_card_card1(self):
        self.assertEqual(self.nine, CardGame.highest_card(self, self.nine, self.five))
    
    def test_highest_card_card2(self):
        self.assertEqual(self.nine, CardGame.highest_card(self, self.five, self.nine))

    def test_cards_total(self):
        self.assertEqual('You have a total of 15', CardGame.cards_total(self, self.hand))

    def test_cards_total_empty(self):
        self.assertEqual('You have a total of 0', CardGame.cards_total(self, []))
