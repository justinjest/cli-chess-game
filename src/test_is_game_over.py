import unittest

from board_logic import generate_starting_board
from board_logic import generate_drawn_board
from board_logic import generate_losing_board
from board_logic import create_board
from turn import is_game_over

class TestIsGameContinuing(unittest.TestCase):
    def test_game_continues(self):
        # Game is not over
        board = generate_starting_board(create_board())
        input = is_game_over(board)
        expect = 0
        self.assertEqual(input, expect)
    def test_game_drawn(self):
        # Game is a draw
        board = generate_drawn_board(create_board())
        input = is_game_over(board)
        expect = 1
        self.assertEqual(input,expect)
    def test_game_loss(self):
        # Game is a loss
        board = generate_losing_board(create_board())
        input = is_game_over(board)
        expect = 2
        self.assertEqual(input, expect)

if __name__ == "__main__":
    unittest.main()