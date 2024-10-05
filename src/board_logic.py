from pieces import *
from render_board import draw_board

# This is where the logic involving game state should live

def create_board():
    board = {}
    for y in range (7, -1, -1):
        for x in range (0, 8):
            board[(x,y)] = ""
    return (board)

def place_pawns(board, x, y, white=True):
    new_board = board
    new_pawn = Pawn ((x,y), white)
    new_board[(x,y)] = new_pawn
    return new_board

def place_rooks(board, x, y, white=True):
    new_board = board
    new_rook = Rook ((x,y), white)
    new_board[(x,y)] = new_rook
    return new_board

def place_knights(board, x, y, white=True):
    new_board = board
    new_knight = Knight((x,y), white)
    new_board[(x,y)] = new_knight
    return new_board

def place_bishops(board, x, y, white=True):
    new_board = board
    new_bishop = Bishop((x,y), white)
    new_board[(x,y)] = new_bishop
    return new_board

def place_queens(board, x, y, white=True):
    new_board = board
    new_queen = Queen((x,y), white)
    new_board[(x,y)] = new_queen
    return new_board

def place_kings(board, x, y, white=True):
    new_board = board
    new_king = King((x,y), white)
    new_board[(x,y)] = new_king
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

def generate_board_no_pawns(board):
    
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

def generate_board_mate(board):
    board = place_kings(board, 4, 0, False)

    board = place_pawns(board, 3, 0, False)
    board = place_pawns(board, 5, 0, False)
    board = place_pawns(board, 3, 1, False)
    board = place_pawns(board, 5, 1, False)
    board = place_pawns(board, 4, 1, False)

    board = place_queens(board, 0, 0, True)
    return board

def generate_board_piece(board):
    board = place_knights(board, 4, 4, False)
    return board

def generate_ambigious_board(board):
    board = place_rooks(board, 0, 7, True)
    board = place_rooks(board, 7, 7, False)
    return board