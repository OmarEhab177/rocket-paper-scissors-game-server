import unittest
from unittest.mock import Mock

from rps_server_game import Player, determine_winner

class TestRPS(unittest.TestCase):
    def test_determine_winner(self):
        player1 = Player(Mock(), Mock())
        player2 = Player(Mock(), Mock())

        player1.choice = 'rock'
        player2.choice = 'scissors'
        winner, choice1, choice2 = determine_winner(player1, player2)
        self.assertEqual(winner, player1)
        self.assertEqual(choice1, 'rock')
        self.assertEqual(choice2, 'scissors')

        player1.choice = 'rock'
        player2.choice = 'paper'
        winner, choice1, choice2 = determine_winner(player1, player2)
        self.assertEqual(winner, player2)
        self.assertEqual(choice1, 'rock')
        self.assertEqual(choice2, 'paper')

        player1.choice = 'scissors'
        player2.choice = 'paper'
        winner, choice1, choice2 = determine_winner(player1, player2)
        self.assertEqual(winner, player1)
        self.assertEqual(choice1, 'scissors')
        self.assertEqual(choice2, 'paper')

if __name__ == '__main__':
    unittest.main()
