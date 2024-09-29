from pieces import *

# TODO: render numbers and letters around edge of board
# TODO: update screen instead of redraw it

def draw_board(board):
    # TODO: turn this into one long string so we can carriage return it
    spacer = " _"
    for i in range(0, 8):
        print (spacer, end = "")
    print ("")
    for y in range(7, -1, -1):
        for x in range (0, 8):
            draw_square(x, y, board)
        print ("")

def draw_square(x, y, board):
    tmp = board[(x,y)]
    piece = draw_piece(tmp)
    if x < 7:
        print (f"|{piece}", end = "")
    if x == 7:
        print(f"|{piece}|", end = "")
        

def draw_piece(piece):
    if isinstance(piece, Piece):
        if piece.white:
            return f'\033[0;30;47m{piece.symbol}\033[0;0m'
        return piece.symbol
    return "_"