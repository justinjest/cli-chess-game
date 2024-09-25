from pieces import *
from render_board import name_column
from render_board import draw_board

# This is where the logic involving game state should live

def create_board():
    board = {}
    for y in range (7, -1, -1):
        for x in range (0, 8):
            board[f"{name_column(x)}{y + 1}"] = ""
    return (board)

def place_pawns(board, x, y):
    white = True
    new_board = board
    board_location = f"{name_column(x)}{y + 1}"
    new_pawn = Pawn (x, y, white)
    new_board[board_location] = new_pawn
    return new_board

board = create_board()
for q in range (0, 8):
    for i in range (0, 8):
        board = place_pawns(board, i, q)

draw_board(board)