from pieces import *
from render_board import name_column
from render_board import draw_board

# This is where the logic involving game state should live

def create_board():
    board = {}
    for y in range (7, -1, -1):
        for x in range (0, 8):
            # Refactor this into a tuple, it will make the piece logic much simpler
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

def place_knights(board, x, y, white=True):
    new_board = board
    board_location = f"{name_column(x)}{y + 1}"
    new_knight = Knight(x, y, white)
    new_board[board_location] = new_knight
    return new_board

def place_bishops(board, x, y, white=True):
    new_board = board
    board_location = f"{name_column(x)}{y + 1}"
    new_bishop = Bishop(x, y, white)
    new_board[board_location] = new_bishop
    return new_board

def place_queens(board, x, y, white=True):
    new_board = board
    board_location = f"{name_column(x)}{y + 1}"
    new_queen = Queen(x, y, white)
    new_board[board_location] = new_queen
    return new_board

def place_kings(board, x, y, white=True):
    new_board = board
    board_location = f"{name_column(x)}{y + 1}"
    new_king = King(x, y, white)
    new_board[board_location] = new_king
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

    board = place_knights(board, 1, 0, True)
    board = place_knights(board, 6, 0, True)
    board = place_knights(board, 1, 7, False)
    board = place_knights(board, 6, 7, False)   

    board = place_bishops(board, 2, 0, True)
    board = place_bishops(board, 5, 0, True)
    board = place_bishops(board, 2, 7, False)
    board = place_bishops(board, 5, 7, False)   
    
    board = place_queens(board, 3, 0, True)
    board = place_queens(board, 3, 7, False)
    board = place_kings(board, 4, 0, True)
    board = place_kings(board, 4, 7, False)
    return board

board = generate_starting_board(create_board())


draw_board(board)