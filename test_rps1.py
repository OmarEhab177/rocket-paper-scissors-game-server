import unittest
from unittest.mock import Mock

from rps_server_game import Player, determine_winner

class TestRPS(unittest.TestCase):
    def test_determine_winner(self):
        player1 = Player(Mock(), Mock())
        player2 = Player(Mock(), Mock())

        player1.choice = 'rock'
        player2.choice = 'scissors'
        winner= determine_winner(player1, player2)
        self.assertEqual(winner, player1)

        player1.choice = 'rock'
        player2.choice = 'paper'
        winner = determine_winner(player1, player2)
        self.assertEqual(winner, player2)

        player1.choice = 'scissors'
        player2.choice = 'paper'
        winner = determine_winner(player1, player2)
        self.assertEqual(winner, player1)

if __name__ == '__main__':
    unittest.main()
