import unittest

from board_logic import generate_starting_board
from board_logic import generate_castle_test
from board_logic import generate_losing_board
from board_logic import create_board
from turn import casteling_left_possible, casteling_right_possible
from player import Player

class TestIsGameContinuing(unittest.TestCase):
    def test_casteling_left_false(self):
        board = generate_starting_board(create_board())
        player = Player(True)
        check = casteling_left_possible(board, player)
        expect = False
        self.assertEqual(check, expect)

    def test_casteling_left_true(self):
        board = generate_castle_test(create_board())
        player = Player(True)
        check = casteling_left_possible(board, player)
        expect = True
        self.assertEqual(check, expect)

    def test_casteling_left_false_b(self):
        board = generate_starting_board(create_board())
        player = Player(False)
        check = casteling_left_possible(board, player)
        expect = False
        self.assertEqual(check, expect)

    def test_casteling_left_true_b(self):
        board = generate_castle_test(create_board())
        player = Player(False)
        check = casteling_left_possible(board, player)
        expect = True
        self.assertEqual(check, expect)

    def test_casteling_right_false(self):
        board = generate_starting_board(create_board())
        player = Player(True)
        check = casteling_right_possible(board, player)
        expect = False
        self.assertEqual(check, expect)

    def test_casteling_right_true(self):
        board = generate_castle_test(create_board())
        player = Player(True)
        check = casteling_right_possible(board, player)
        expect = True
        self.assertEqual(check, expect)

    def test_casteling_right_false_b(self):
        board = generate_starting_board(create_board())
        player = Player(False)
        check = casteling_right_possible(board, player)
        expect = False
        self.assertEqual(check, expect)

    def test_casteling_right_true_b(self):
        board = generate_castle_test(create_board())
        player = Player(False)
        check = casteling_right_possible(board, player)
        expect = True
        self.assertEqual(check, expect)