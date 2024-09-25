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

def place_pawns(board, x, y, white=True):
    new_board = board
    board_location = f"{name_column(x)}{y + 1}"
    new_pawn = Pawn (x, y, white)
    new_board[board_location] = new_pawn
    return new_board

def place_rooks(board, x, y, white=True):
    new_board = board
    board_location = f"{name_column(x)}{y + 1}"
    new_rook = Rook(x, y, white)
    new_board[board_location] = new_rook
    return new_board

def generate_starting_board(board):
    # Place pawns
    for i in range(0, 8):
        board = place_pawns(board, i, 1, True)
    
    for y in range(0, 8):
        board = place_pawns(board, y, 6, False)

    board = place_rooks(board, 0, 0, True)
    board = place_rooks(board, 7, 0, True)
    board = place_rooks(board, 0, 7, False)
    board = place_rooks(board, 7, 7, False)
    return board

board = generate_starting_board(create_board())


draw_board(board)