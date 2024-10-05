import unittest

from board_logic import generate_starting_board
from board_logic import create_board
from turn import is_game_over

class TestIsGameOver(unittest.TestCase):
    def test_eq(self):
        # Game is not over
        board = generate_starting_board(create_board())
        input = is_game_over(board)
        expect = 0
        self.assertEqual(input, expect)


if __name__ == "__main__":
    unittest.main()